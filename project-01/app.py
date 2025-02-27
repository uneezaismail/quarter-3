import streamlit as st

st.markdown("""
    <style>
        body {
            font-family: 'Open Sans', sans-serif;
            background-color: #E0F2F1;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 16px;
            color: #ffffff;
            text-align: center;
            background: linear-gradient(90deg, #00897B, #00695C);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .result-box {
            background: #B2DFDB;
            padding: 15px;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            border-radius: 8px;
            margin-top: 20px;
            color: #00695C;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .reference-box {
            background: #FFFFFF;
            padding: 15px;
            font-size: 18px;
            text-align: center;
            border-radius: 8px;
            margin-top: 20px;
            color: #00897B;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .sidebar {
            background-color: #00897B;
            color: #FFFFFF;
        }
        .sidebar .sidebar-content .block-container {
            padding-top: 20px;
        }
        .sidebar .sidebar-content h3 {
            color: #B2DFDB;
        }
           .sidebar-content {
                background-color: #004D40;  /* Deep teal */
                padding: 20px;
                border-radius: 10px;
                color: white;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            }
            .sidebar-title {
                font-size: 22px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 15px;
                color: #B2DFDB;
            }
            .history-item {
                background: #ffffff;  /* Medium teal */
                padding: 10px;
                border-radius: 6px;
                margin-bottom: 5px;
                font-size: 16px;
                color: black;
                text-align: center;
                box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.1);
            }
            .clear-button {
                display: flex;
                justify-content: center;
                margin-top: 15px;
            }
    </style>
""", unsafe_allow_html=True)

# Conversion Factors
conversion_factors = {
    "Length": {
        "Meter": 1, 
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000, 
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1e6,
        "Pound": 2.20462,
        "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x * 9/5) + 32,
        "Kelvin": lambda x: x + 273.15
    },
    "Volume": {
        "Liter": 1,
        "Milliliter": 1000,
        "Gallon": 0.264172,
        "Cubic Meter": 0.001,
        "Cup": 4.16667
    },
    "Time": {
        "Second": 1,
        "Minute": 1/60,
        "Hour": 1/3600,
        "Day": 1/86400
    },
    "Speed": {
        "Meter per Second": 1,
        "Kilometer per Hour": 3.6,
        "Miles per Hour": 2.23694
    },
    "Pressure": {
        "Pascal": 1,
        "Kilopascal": 0.001,
        "Bar": 0.00001,
        "PSI": 0.000145038,
        "mmHg": 0.00750062
    }
}


# Function to get conversion formula
def get_conversion_formula(category, from_unit, to_unit):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return "multiply by 9/5, then add 32"
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return "add 273.15"
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return "subtract 32, then multiply by 5/9"
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return "subtract 273.15"
        else:
            return "use complex formula (see full reference)"
    else:
        factor = conversion_factors[category][to_unit] / conversion_factors[category][from_unit]
        if factor > 1:
            return f"multiply the {category.lower()} value by {factor:.6g}"
        else:
            return f"divide the {category.lower()} value by {1/factor:.6g}"


# Title
st.markdown("<div class='title'>📐 Unit Converter</div>", unsafe_allow_html=True)


# Select Conversion Type
category = st.selectbox("📏Select Conversion Type", list(conversion_factors.keys()))


# Select Units
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", list(conversion_factors[category].keys()))
with col2:
    to_unit = st.selectbox("To", list(conversion_factors[category].keys()))


# Input Value
value = st.number_input("📝 Enter Value", min_value=0.0, step=0.1, format="%.2f")

   
# History Management
if 'history' not in st.session_state:
    st.session_state.history = []

# Perform Conversion
if st.button("Convert", key="convert", help="Click to convert the value"):
    if category == "Temperature":
        if from_unit == "Celsius":
            result = conversion_factors["Temperature"][to_unit](value)
        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
            result = conversion_factors["Temperature"][to_unit](celsius)
        elif from_unit == "Kelvin":
            celsius = value - 273.15
            result = conversion_factors["Temperature"][to_unit](celsius)
    else:
        result = value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])
    

    # Store history
    conversion_entry = f"{value} {from_unit} = {result:.4f} {to_unit}"
    st.session_state.history.append(conversion_entry)
    

    # Display Result
    st.markdown(f"<div class='result-box'>✅ Result: {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
    

    # Display Formula
    formula = get_conversion_formula(category, from_unit, to_unit)
    st.markdown(f"""
    <div class='reference-box'>
        <h3>Formula</h3>
        <p>{formula}</p>
    </div>
    """, unsafe_allow_html=True)


# Display History in Sidebar
with st.sidebar:
    st.markdown("### 📜 Conversion History")
    if st.session_state.history:
        for item in st.session_state.history[-5:]: 
            st.markdown(f"<div class='history-item'>{item}</div>", unsafe_allow_html=True)

        if st.button("🗑 Clear History", key="clear_history"):
            st.session_state.history = []
    else:
        st.markdown("<p style='text-align: center; color: #004D40;'>No conversions yet! 😊</p>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)   