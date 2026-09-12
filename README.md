# Real Estate Price Prediction

A machine learning application that estimates house prices from property details such as area, bedrooms, bathrooms, stories, parking, road access, and furnishing status.

The project uses:

- Streamlit for the interactive web interface
- FastAPI for the prediction API
- A Random Forest regression model trained with scikit-learn

## Features

- Interactive property inputs
- House price prediction
- Price category: low range, mid range, or high range
- Property profile classification
- Dark, responsive Streamlit interface

## Project Structure

```text
frontend.py       Streamlit user interface
app.py            FastAPI prediction service
train_model.py   Model training script
Housing.csv      Housing dataset
house_model.pkl  Saved trained model
README.md        Project documentation
```

## Installation

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install streamlit fastapi uvicorn requests joblib numpy pandas scikit-learn
```

## Run the Application

Open two terminals in the project folder.

### 1. Start the FastAPI backend

```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### 2. Start the Streamlit frontend

```bash
streamlit run frontend.py
```

The Streamlit application will open in your browser, usually at:

```text
http://localhost:8501
```

## API Endpoint

### `POST /predict`

Example request:

```json
{
  "area": 1200,
  "bedrooms": 3,
  "bathrooms": 2,
  "stories": 2,
  "parking": 1,
  "mainroad": true,
  "furnishingstatus": "semi-furnished"
}
```

Example response:

```json
{
  "predicted_price": 6055181.0,
  "predicted_category": "mid range"
}
```

## Retrain the Model

To train the model again using `Housing.csv`, run:

```bash
python train_model.py
```

This regenerates `house_model.pkl`.

## Deployment Note

GitHub stores the project files but does not run the application. For deployment, host the Streamlit frontend on Streamlit Community Cloud and the FastAPI backend on a service such as Render or Railway.

Before deploying the frontend, replace the local API address in `frontend.py`:

```python
http://127.0.0.1:8000/predict
```

with the public URL of the deployed FastAPI service.

## License

This project is for educational and demonstration purposes.
