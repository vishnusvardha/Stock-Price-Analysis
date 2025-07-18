from flask import Flask, request, jsonify

import joblib
import logging
import os
from flask_cors import CORS
import pandas as pd
import yfinance as yf
import numpy as np

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)

# Load the trained stock price prediction model
model_bundle = None
model_path = 'model.pkl'
try:
    if not os.path.exists(model_path):
        logging.error(f"Model file not found at {model_path}")
    else:
        model_bundle = joblib.load(model_path)
        logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load model: {e}")


@app.route('/health', methods=['GET'])
def health():
    if model_bundle is not None:
        return jsonify({'status': 'ok'}), 200
    else:
        return jsonify({'status': 'model not loaded'}), 500




@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        logging.debug(f"POST request json: {data}")
        if not data or 'symbol' not in data:
            msg = "No stock symbol provided"
            logging.error(msg)
            return jsonify({'error': msg}), 400

        symbol = data['symbol'].upper()
        # Fetch recent stock data (last 2 months)
        stock = yf.Ticker(symbol)
        hist = stock.history(period="2mo")
        if hist.empty or len(hist) < 2:
            return jsonify({'error': f'Not enough data for symbol {symbol}'}), 400

        # Use the last close as the "prediction"
        last_row = hist.iloc[-1]
        predicted_price = float(last_row['Close'])
        closes = hist['Close'].tail(10).tolist()

        return jsonify({'predicted_price': predicted_price, 'history': closes})
    except Exception as e:
        logging.error(f"Error during prediction: {e}", exc_info=True)
        return jsonify({'error': f"Error during prediction: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
    
           
