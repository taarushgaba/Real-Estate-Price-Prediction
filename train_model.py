import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Load dataset
df = pd.read_csv("Housing.csv")

# Keep selected columns
df = df[
    ['price', 'area', 'bedrooms', 'bathrooms',
     'stories', 'parking', 'mainroad', 'furnishingstatus']
]

# Encode categorical columns
df['mainroad'] = LabelEncoder().fit_transform(df['mainroad'])
df['furnishingstatus'] = LabelEncoder().fit_transform(df['furnishingstatus'])

# Split features and target
X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=None,
    random_state=42
)
model.fit(X_train, y_train)



# Save model
joblib.dump(model, "house_model.pkl")

print("Model trained and saved successfully!")