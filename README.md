# Stock Price Prediction Web App

This project is a simple web application that allows users to enter a stock symbol (e.g., AAPL, MSFT) and view the latest stock price along with a chart of recent prices. The app fetches live data using Yahoo Finance and displays it in a modern, user-friendly interface.

## Features
- Enter any stock symbol to get the latest price
- Interactive chart showing the last 10 closing prices plus the latest price
- Clean, responsive frontend (HTML/CSS/JavaScript)
- Python Flask backend fetches live data from Yahoo Finance (via yfinance)
- No machine learning model required

## How It Works
1. **Frontend**: User enters a stock symbol and submits the form.
2. **Backend**: Flask receives the symbol, fetches recent price data from Yahoo Finance, and returns the latest price and price history.
3. **Frontend**: Displays the predicted/latest price and updates the chart.

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package manager)

### 1. Install Python dependencies
Open a terminal in the project folder and run:
```
pip install flask flask-cors yfinance pandas
```

### 2. Start the Flask backend
In the same folder, run:
```
python app.py
```
This will start the backend server on `http://localhost:5000`.

### 3. Serve the frontend
Open a new terminal in the same folder and run:
```
python -m http.server 8000
```
This will serve your frontend files on `http://localhost:8000`.

### 4. Open the app in your browser
Go to:
```
http://localhost:8000/index.html
```

## Usage
- Enter a valid stock symbol (e.g., AAPL for Apple, MSFT for Microsoft) and click "Predict Price".
- The app will display the latest closing price and a chart of the last 10 closes plus the latest price.

## Notes
- The "prediction" is simply the latest available closing price from Yahoo Finance.
- The backend can be extended to use a real machine learning model for future price prediction if desired.
- If you see CORS or network errors, make sure both the backend and frontend servers are running as described above.

## Example Symbols
- AAPL (Apple)
- MSFT (Microsoft)
- TSLA (Tesla)
- AMZN (Amazon)
- GOOGL (Alphabet/Google)

## License
This project is for educational/demo purposes. Use at your own risk.
