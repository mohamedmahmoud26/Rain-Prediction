# Rain Prediction Project - Team SkyCast

## Project Overview

The Rain Prediction Project aims to build an intelligent model capable of predicting whether it will rain tomorrow based on real-world weather data collected from Australian weather stations.  
The project leverages machine learning techniques to analyze various meteorological features such as temperature, humidity, wind speed, air pressure, and more, in order to make accurate predictions that assist in weather forecasting.
---


ividuals**: Planning their day, choosing appropriate clothing, or deciding whether to carry an umbrella.
- **Agriculture**: Scheduling irrigation and harvesting.
- **Transportation**: Minimizing risks caused by weather conditions.

### Our main goal is:
**To build a smart system that predicts whether it will rain tomorrow based on today’s weather data.**
---

## How to Run the Project Locally

Follow the steps below to run the Rain Prediction app on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/B-MEbrahim/Rain-Prediction.git
cd Rain-Prediction
```

### 2. (Optional) Create and Activate a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App
```bash
streamlit run app.py
```
------

To run this project, make sure you have the following installed:

- Python 3.8 or higher
- pandas
- numpy
- scikit-learn
- xgboost
- imbalanced-learn
- streamlit
- matplotlib (optional, for data visualization)
- seaborn (optional, for data visualization)
------
## Usage Example

Once the app is running, you can:

1. View the main page and read project details.
2. Upload a CSV file with weather data, or use the default sample.
3. Click the "Predict" button to see if it will rain tomorrow.
4. Explore the results, prediction, and model performance.

Example CSV format:
```csv
MinTemp,MaxTemp,Rainfall,Humidity3pm,Pressure3pm,RainToday
14.0,24.3,0.0,44,1015.0,No
13.7,23.4,0.0,38,1012.8,No
...
```

Expected output:
```
Prediction: It will NOT rain tomorrow 
```
or
```
Prediction: It WILL rain tomorrow
```
-------------
## Useful Links

- **GitHub Repository:**  
  [https://github.com/B-MEbrahim/Rain-Prediction](https://github.com/B-MEbrahim/Rain-Prediction)

- **Kaggle Notebook (EDA & Modeling):**  
  [https://www.kaggle.com/code/mohamedmahmoud111/rain-prediction-porject](https://www.kaggle.com/code/mohamedmahmoud111/rain-prediction-porject)

- **Live Streamlit App:**  
  [https://rain-prediction-xynsjsyukgjsyykngqqgqy.streamlit.app/](https://rain-prediction-xynsjsyukgjsyykngqqgqy.streamlit.app/)
## Team Members

- Hassan Abdelrazek 
- Mahmoud Ebrahim  
- Mohamed Elseragy
- Ahmed Fouad  
- Abdulrhman Hosny  
- Wageeh Abdelhameed  
