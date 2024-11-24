import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression


# Example data loading

data = pd.read_csv('Metro_Interstate_Traffic_Volume.csv')
data['hour'] = pd.to_datetime(data['date_time']).dt.hour
data['holiday'] = data['holiday'].apply(lambda x: 0 if x == 'None' else 1)

# Features and target
X = data[['hour', 'temp', 'holiday']]
y = data['traffic_volume']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = RandomForestRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Streamlit UI
st.title("Traffic Volume Predictor")
# Sidebar
st.sidebar.title("User Input")
y_pred = model.predict(X_test)

hour = st.sidebar.slider("Hour of the day", 0, 23, 12)  # Slider for hour input
temp = st.sidebar.slider("Temperature", -20, 40, 20)  # Slider for temperature input
holiday = st.sidebar.selectbox("Holiday", ['None', 'Holiday'])  # Selectbox for holiday input

# Update the 'holiday' value (0 or 1)
holiday = 0 if holiday == 'None' else 1


# Scatter plot
st.write("### Actual vs Predicted with Regression Line")
max_val = max(max(y_test), max(y_pred))
min_val = min(min(y_test), min(y_pred))

fig, ax = plt.subplots(figsize=(10, 10))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6, label='Predictions', ax=ax)
sns.regplot(x=y_test, y=y_pred, scatter=False, ci=None, color='red', label='Regression Line', ax=ax)
ax.plot([min_val, max_val], [min_val, max_val], color='green', linestyle='--', label='Perfect Prediction Line')
ax.set_xlabel('Actual Traffic Volume')
ax.set_ylabel('Predicted Traffic Volume')
ax.legend()

# Predict traffic volume based on user input
user_input = np.array([[hour, temp, holiday]])
user_prediction = model.predict(user_input)

# Display the prediction
st.write(f"Predicted Traffic Volume for Hour {hour} with Temp {temp}°C and Holiday={holiday}: {user_prediction[0]:.2f}")
st.pyplot(fig)



st.write("### Scatter Plots: Relationships with Traffic Volume")

# Scatter plot for 'hour' vs 'traffic_volume'
df = data[['hour', 'temp', 'holiday', 'traffic_volume']]

fig, ax = plt.subplots()
sns.scatterplot(x=df['hour'], y=df['traffic_volume'], ax=ax)
ax.set_title('Traffic Volume vs Hour')
st.pyplot(fig)

# Scatter plot for 'temp' vs 'traffic_volume'
fig, ax = plt.subplots()
data['temp'] = data['temp'] - 273.15
sns.scatterplot(x=df['temp']-273.15, y=df['traffic_volume'], ax=ax)
ax.set_title('Traffic Volume vs Temperature')
st.pyplot(fig)

# Box plot for 'holiday' vs 'traffic_volume'
fig, ax = plt.subplots()
sns.boxplot(x=df['holiday'], y=df['traffic_volume'], ax=ax)
ax.set_title('Traffic Volume on Holidays vs Non-Holidays')
st.pyplot(fig)

