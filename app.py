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

# 读取Excel文件获取参数配置
def get_parameters():
    try:
        df = pd.read_excel('test.xlsx', engine='openpyxl')
        if df.empty:
            raise ValueError('Excel file is empty')
        # 过滤掉Unnamed列
        return [col for col in df.columns.tolist() if not col.startswith('Unnamed')]  # 返回参数名称列表
    except FileNotFoundError:
        raise ValueError('test.xlsx file not found')
    except Exception as e:
        raise ValueError(f'Error reading Excel file: {str(e)}')

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
        
        # 转换为numpy数组
        features = np.array(data).reshape(1, -1)
        
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
