// 获取参数配置并生成输入框
async function initInputs() {
    try {
        const response = await fetch('/parameters');
        if (!response.ok) {
            throw new Error('Failed to get parameters');
        }
        
        const { parameters } = await response.json();
        const container = document.getElementById('input-container');
        
        // 清空现有输入框
        container.innerHTML = '';
        
        // 为每个参数生成输入框
        parameters.forEach((param, index) => {
            const div = document.createElement('div');
            div.className = 'input-group';
            
            const label = document.createElement('label');
            label.textContent = param + ':';
            label.htmlFor = `feature${index}`;
            
            const input = document.createElement('input');
            input.type = 'number';
            input.step = 'any';
            input.id = `feature${index}`;
            input.required = true;
            
            div.appendChild(label);
            div.appendChild(input);
            container.appendChild(div);
        });
    } catch (error) {
        console.error('Error initializing inputs:', error);
    }
}

// 初始化输入框
initInputs();

document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // 获取所有输入值
    const inputs = document.querySelectorAll('#input-container input');
    const features = Array.from(inputs).map(input => parseFloat(input.value));
    
    try {
        // 调用后端API
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ features })
        });
        
        if (!response.ok) {
            throw new Error('Prediction failed');
        }
        
        const data = await response.json();
        
        // 显示预测结果
        const resultElement = document.getElementById('prediction-result');
        const prediction = data.prediction;
        if (prediction > 0.45) {
            resultElement.textContent = 'CRC';
            resultElement.className = 'crc';
        } else {
            resultElement.textContent = 'CD';
            resultElement.className = 'cd';
        }
        
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('prediction-result').textContent = 'Error: ' + error.message;
    }
});
