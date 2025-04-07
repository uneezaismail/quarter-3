import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart BMI Calculator", page_icon="💪", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        .header-container {
            background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
            padding: 15px;
            border-radius: 15px;
            margin-bottom: 25px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            text-align: center;
        }
        .result-container {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            text-align: center;
        }
        .bmi-table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        .bmi-table th, .bmi-table td {
            padding: 12px;
            text-align: center;
            font-size: 16px;
            border: 1px solid #eaeaea;
        }
        .bmi-table th {
            background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
            color: white;
            font-weight: 600;
        }
        .bmi-table tr:nth-child(even) {
            background: #f8f9fa;
        }
        .bmi-table tr:hover {
            background: #f1f3f5;
        }
        .stButton>button {
            background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-weight: bold;
            border: none;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            width: 100%;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0,0,0,0.15);
        }
        .advice-box {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #4b6cb7;
            margin: 10px 0;
        }
        .stNumberInput > div > div > input {
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
        <h1 style='color: white; margin-bottom: 0;'>💪 Smart BMI Calculator</h1>
        <p style='color: #c3cfe2; margin-top: 5px;'>Your personal health companion</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div>
        <h3>🏋️ Enter Your Details</h3>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    height = st.number_input("📏 Enter your height (cm):", min_value=80, max_value=250, value=175, step=1)
with col2:
    weight = st.number_input("⚖️ Enter your weight (kg):", min_value=20, max_value=200, value=70, step=1)

if st.button("⚖️ Get Your BMI Score"):
    bmi = weight / ((height / 100) ** 2)

    if bmi < 18.5:
        category, color, advice, emoji = "Underweight", "#3498db", "Consider eating a nutrient-rich diet. 🍽️", "📉"
    elif 18.5 <= bmi < 24.9:
        category, color, advice, emoji = "Normal Weight", "#2ecc71", "Great job! Maintain a balanced diet. ✅", "🥳"
    elif 25 <= bmi < 29.9:
        category, color, advice, emoji = "Overweight", "#f39c12", "Incorporate more activity and a healthy diet. 🏃‍♂️🥗", "📈"
    else:
        category, color, advice, emoji = "Obesity", "#e74c3c", "Consult a healthcare professional for guidance. 💡", "🚀"

    st.markdown(f"""
        <div class="result-container">
            <h2 style=' margin-bottom: 5px;'>Your BMI is <span style='color:{color}; margin-bottom: 5px;'>{bmi:.2f}</span></h2>
            <h3 style='color:{color}; margin-top: 0;'>{emoji} You are {category}</h3>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <h3 style='color:#182848; margin-top: 20px;'>📊 BMI Categories</h3>
    <table class="bmi-table">
        <tr>
            <th>Category</th>
            <th>BMI Range</th>
            <th>Color Code</th>
        </tr>
        <tr>
            <td>Underweight</td>
            <td>&lt; 18.5</td>
            <td><span style="color: #3498db; font-weight: bold;">🔵 Blue</span></td>
        </tr>
        <tr>
            <td>Normal Weight</td>
            <td>18.5 - 24.9</td>
            <td><span style="color: #2ecc71; font-weight: bold;">🟢 Green</span></td>
        </tr>
        <tr>
            <td>Overweight</td>
            <td>25 - 29.9</td>
            <td><span style="color: #f39c12; font-weight: bold;">🟠 Orange</span></td>
        </tr>
        <tr>
            <td>Obesity</td>
            <td>30+</td>
            <td><span style="color: #e74c3c; font-weight: bold;">🔴 Red</span></td>
        </tr>
    </table>
""", unsafe_allow_html=True)

st.markdown("""
    <div>
            <hr/>
        <h6 style='text-align: center'>Stay Healthy, Stay Fit! 💖</h6>
    </div>
""", unsafe_allow_html=True)
