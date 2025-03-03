from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
import pandas as pd

app = Flask(__name__)

# 加载模型
with open('PR1_prediction_results_20241127171144.pkl', 'rb') as f:
    model = pickle.load(f)

# 特征处理
poly = PolynomialFeatures(degree=1)
scaler = StandardScaler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parameters')
def parameters():
    try:
        params = get_parameters()
        return jsonify({
            'parameters': params
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 固定参数配置
def get_parameters():
    return {
        '1. Sex(Male=1, Female=0)': 0,
        '2. Age': 59,
        '3. FC': 15,
        '4. FIT(Positive=1, Negative=0)': 1,
        '5. KRAS(Positive= Ct value, Negative=0)': 0,
        '6. BMP3(Positive= Ct value, Negative=0)': 38,
        '7. NDRG4(Positive= Ct value, Negative=0)': 29,
        '8. SDC2(Positive= Ct value, Negative=0)': 0
    }

def calculate_gene_value(ct, base_ct):
    """计算基因表达值"""
    if ct is None or ct == 0:  # Negative
        return 0
    return (1/2) ** (ct - base_ct)

def preprocess_features(features):
    """预处理特征值"""
    # 转换Sex和FIT为数值
    features[0] = 1 if features[0] == 'Male' else 0  # Sex
    features[3] = 1 if features[3] == 'Positive' else 0  # FIT
    
    # 计算基因表达值
    features[4] = calculate_gene_value(features[4], 30)  # KRAS
    features[5] = calculate_gene_value(features[5], 50)  # BMP3
    features[6] = calculate_gene_value(features[6], 50)  # NDRG4
    features[7] = calculate_gene_value(features[7], 21)  # SDC2
    
    return features

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 获取前端输入
        data = request.json['features']
        
        # 验证输入参数数量
        expected_params = get_parameters()
        if len(data) != len(expected_params):
            return jsonify({
                'error': f'Expected {len(expected_params)} parameters, got {len(data)}'
            }), 400
        
        # 预处理特征值
        processed_data = preprocess_features(data)
        
        # 转换为numpy数组
        features = np.array(processed_data).reshape(1, -1)
        
        # 特征处理
        features_poly = poly.fit_transform(features)
        features_scaled = scaler.fit_transform(features_poly)
        
        # 预测
        prediction = model.predict(features_scaled)[0]
        
        return jsonify({
            'prediction': float(prediction),
            'parameters': expected_params
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
