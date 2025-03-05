
import streamlit as st

# Function for conversion
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
    }

    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        conversion_factor = conversions[key]
        return value * conversion_factor
    else:
        return "🚫 Conversion not supported!"

# Custom CSS for styling
st.markdown("""
    <style>
        /* Subheader */
        .subheader {
            font-size: 28px;
            font-weight: bold;
            color: #FF1493; /* Deep Pink */
            font-family: 'Arial', sans-serif;
            font-style: italic;
        }

        /* Glassmorphism Input */
        .stTextInput, .stNumberInput, .stSelectbox {
            background: rgba(255, 255, 255, 0.2) !important;
            border-radius: 15px !important;
            padding: 10px !important;
            border: 1px solid #FF69B4 !important;
            backdrop-filter: blur(10px) !important;
            transition: 0.3s ease-in-out !important;
        }

        /* Hover Effect on Inputs */
        .stTextInput:hover, .stNumberInput:hover, .stSelectbox:hover {
            border-color: #C71585 !important;
            box-shadow: 0px 0px 10px rgba(199, 21, 133, 0.6) !important;
        }

        /* Convert Button */
        .convert-btn {
            background-color: #FF1493 !important; /* Deep Pink */
            color: white !important;
            border-radius: 12px !important;
            padding: 15px !important;
            font-size: 24px !important;
            font-weight: bold !important;
            width: 100% !important;
            text-align: center !important;
            cursor: pointer !important;
            border: none !important;
            font-style: italic !important;
        }

        .convert-btn:hover {
            background-color: #C71585 !important; /* Medium Violet Red */
        }

        /* Result Text */
        .result-text {
            font-size: 30px !important;
            font-weight: bold !important;
            color: rgb(255, 27, 217) !important; /* Pink */
            font-family: 'Arial', sans-serif !important;
            font-style: italic !important;
        }
    </style>
""", unsafe_allow_html=True)

# 🎯 Stylish Title with **Forced Inline CSS** 
st.markdown('<h1 style="text-align: center; font-size: 50px; font-weight: bold; color: #FF1493; font-family: Arial, sans-serif; font-style: italic;">🔢 Unit Converter 🔄</h1>', unsafe_allow_html=True)

st.markdown('<p class="subheader">📌 <i>Enter your values below:</i></p>', unsafe_allow_html=True)

# 🛠 User Input
value = st.number_input("✏️ *Enter the value:*" , min_value=1.0, step=1.0)
unit_from = st.selectbox("🔄 *Convert from:*", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("🎯 *Convert to:*", ["meters", "kilometers", "grams", "kilograms"])

# 🚀 Convert Button
if st.button("🔥 Convert Now 🔄", key="convert_btn", help="Click to convert the units"):
    result = convert_units(value, unit_from, unit_to)
    st.markdown(f'<p class="result-text">✅ Converted Value: <span style="color: blue;">{result}</span> 🎉</p>', unsafe_allow_html=True)




