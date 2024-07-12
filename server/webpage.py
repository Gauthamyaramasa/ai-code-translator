from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this import
from app import set_api_key, set_model, convert_code

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/set-api-key', methods=['POST'])
def api_key():
    data = request.get_json()
    api_key = data.get('api_key')
    if api_key:
        set_api_key(api_key)
        return jsonify({"message": "API key set successfully"}), 200
    else:
        return jsonify({"error": "API key is required"}), 400

@app.route('/set-model', methods=['POST'])
def model():
    data = request.get_json()
    model_name = data.get('model_name')
    if model_name:
        set_model(model_name)
        return jsonify({"message": "Model set successfully"}), 200
    else:
        return jsonify({"error": "Model name is required"}), 400

@app.route('/convert-code', methods=['POST'])
def convert():
    data = request.get_json()
    input_code = data.get('input_code')
    input_lang = data.get('input_lang')
    output_lang = data.get('output_lang')
    if input_code and input_lang and output_lang:
        result = convert_code(input_code, input_lang, output_lang)
        if result:
            return jsonify({"converted_code": result}), 200
        else:
            return jsonify({"error": "Code conversion failed"}), 500
    else:
        return jsonify({"error": "Input code, input language, and output language are required"}), 400

if __name__ == '__main__':
    app.run(debug=True)
