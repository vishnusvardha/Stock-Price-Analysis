import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load the stock dataset
df = pd.read_csv('infolimpioavanzadoTarget.csv')


# Assume the last column is the target (stock price), others are features
X = df.iloc[:, :-1]
y = df.iloc[:, -1]


# Remove non-numeric columns (e.g., dates, text)
X = X.select_dtypes(include=['number'])
print('Columns used for training:', X.columns.tolist())

# Replace inf/-inf with NaN, then fill NaN with column mean
import numpy as np
X = X.replace([np.inf, -np.inf], np.nan)
num_missing = X.isnull().sum().sum()
if num_missing > 0:
    print(f'Filling {num_missing} missing values with column means.')
    X = X.fillna(X.mean())

# Final check for any remaining NaN or inf
if np.isinf(X.values).any() or np.isnan(X.values).any():
    print('Warning: There are still NaN or infinite values in the features!')

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and feature columns
joblib.dump({'model': model, 'columns': X.columns.tolist()}, 'model.pkl')

print('Stock price prediction model trained and saved as model.pkl')
