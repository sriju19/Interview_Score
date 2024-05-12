import streamlit as st
import joblib 
import pandas as pd

# Load the model
model, ref_col, target = joblib.load("model.pkl")

# Set page title and icon
st.set_page_config(page_title="Salary Predictor", page_icon="💰")

# Sidebar navigation
nav = st.sidebar.radio("Navigation", ["Predict", "Contribute"])

# Title and introduction
st.title("Salary Predictor")
st.write("Welcome to the Salary Predictor app! This tool helps you estimate your salary based on your experience, test score, and interview score.")

if nav == "Predict":
    st.image("salary-calculator.png", use_column_width=True)
    # Take user input
    with st.form("prediction_form"):
        st.header("Enter Your Details")
        n = st.slider("Years of Experience", 0, 20)
        m = st.number_input("Test Score", step=1.0)
        p = st.number_input("Interview Score", step=1.0)
        submit_button = st.form_submit_button(label="Predict Salary")
    
    # Predict based on user input
    if submit_button:
        prediction = model.predict([[n, m, p]])
        st.success(f"Your predicted salary is ${round(prediction[0], 2)}")
else:
    st.subheader("Contribute")
    st.write("Have more data to improve predictions? Feel free to contribute!")
    ex = st.number_input("Enter your Experience",0.0,20.0, step=1.0)
    sal = st.number_input("Enter your Salary",0.00,1000000.00,step = 1000.0)
    if st.button("submit"):
        to_add = {"YearsExperience":[ex],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("Salary_Data.csv",mode='a',header = False,index= False)
        st.success("Submitted")

# Add some style with light colors and clean design
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        color: #333333;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    .st-bm {
        background-color: #ffffff;
    }
    .st-bn {
        color: #333333;
    }
    .st-ax {
        font-family: "Arial", sans-serif;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)
