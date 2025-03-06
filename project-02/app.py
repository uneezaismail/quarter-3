import streamlit as st
import random
import string
import re

st.set_page_config(
    page_title="Password strength meter",
    page_icon="🔐",
    layout="centered"
)


theme_css = """
<style>
    body {
        background-color: #121212;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    .main {
        padding: 2rem;
    }
    .stTextInput>div>div>input {
        border-radius: 0.5rem;
        padding: 0.5rem;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff6b6b, #f06595);
        color: white;
        border-radius: 0.5rem;
        padding: 0.6rem 1.2rem;
        font-size: 1rem;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #f06595, #ff6b6b);
        color: white;
    }
    .stButton>button:active {
        background: white !important;
        color: #f06595 !important;
    }
    .password-output {
        color: #282828;
        background-color: #D3D3D3;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
        font-family: monospace;
        font-size: 1.2rem;
        word-break: break-all;
    }
    .strength-meter {
        height: 0.5rem;
        border-radius: 0.25rem;
        margin-top: 0.5rem;
        transition: all 0.3s ease;
    }
    .feedback-item {
        margin-bottom: 0.25rem;
        color: #ff6b6b;
    }
    .strength-text {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    
</style>
"""
st.markdown(theme_css, unsafe_allow_html=True)

def check_password_strength(password):
    """Check the strength of a password and provide feedback."""
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 1
    elif len(password) >= 8:
        feedback.append("❌ Consider using at least 12 characters for a stronger password.")
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")
    
    if re.search(r"[!@#$%^&*()_+\-=[\]{};'\"\\|<>/?]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character.")
    
    strength_labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_colors = ["#ff4e50", "#ffa700", "#ffff00", "#aaff00", "#00e676"]
    strength_classes = ["very-weak", "weak", "moderate", "strong", "very-strong"]
    
    strength_index = min(score, 4)
    strength_text = strength_labels[strength_index]
    strength_color = strength_colors[strength_index]
    strength_class = strength_classes[strength_index]
    
    return score, feedback, strength_text, strength_color, strength_class

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    """Generate a password based on specified criteria."""
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not characters:
        return "Please select at least one character type."

    max_attempts = 1000
    best_password = ""
    best_score = -1

    for _ in range(max_attempts):
        password = ''.join(random.choice(characters) for _ in range(length))
        score, _, strength_text, _, _ = check_password_strength(password)
        
        if score > best_score:
            best_password = password
            best_score = score

        if strength_text == "Very Strong":
            return password

    return best_password  


st.title("🔐 Password Checker & Generator")


tab1, tab2 = st.tabs(["Check Strength", "Generate Password"])


with tab1:
    st.header("Check Password Strength")
    
    password_to_check = st.text_input("Enter a password to check", type="password")
    
    if st.button("Check Strength"):
        if password_to_check:
            score, feedback, strength_text, strength_color, strength_class = check_password_strength(password_to_check)
            
            
            st.markdown(f"<p class='strength-text'><span class='{strength_class}'>Strength: {strength_text}</span></p>", unsafe_allow_html=True)
            st.markdown(f"<div class='strength-meter' style='width: {score*25}%; background-color: {strength_color};'></div>", unsafe_allow_html=True)
            
            if feedback:
                st.subheader("Suggestions for improvement:")
                for item in feedback:
                    st.markdown(f"<div class='feedback-item'>{item}</div>", unsafe_allow_html=True)
            else:
                st.success("Great! Your password is very strong.")
        else:
            st.warning("Please enter a password to check.")


with tab2:
    st.header("Generate a Strong Password")
    
    length = st.slider("Password Length", min_value=8, max_value=32, value=16)
    
    col1, col2 = st.columns(2)
    with col1:
        use_uppercase = st.checkbox("Uppercase Letters", value=True)
        use_lowercase = st.checkbox("Lowercase Letters", value=True)
    with col2:
        use_numbers = st.checkbox("Numbers", value=True)
        use_symbols = st.checkbox("Symbols", value=True)
    
    if st.button("Generate Password"):
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
        
        if password == "Please select at least one character type.":
            st.warning(password)
        else:
            st.markdown(f"<div class='password-output'>{password}</div>", unsafe_allow_html=True)
            
            
            score, feedback, strength_text, strength_color, strength_class = check_password_strength(password)
            st.markdown(f"<p class='strength-text'><span class='{strength_class}'>Strength: {strength_text}</span></p>", unsafe_allow_html=True)
            st.markdown(f"<div class='strength-meter' style='width: {score*25}%; background-color: {strength_color};'></div>", unsafe_allow_html=True)
            
            if feedback:
                st.subheader("Suggestions for improvement:")
                for item in feedback:
                    st.markdown(f"<div class='feedback-item'>{item}</div>", unsafe_allow_html=True)
            else:
                st.success("Great! Your password is very strong.")

st.markdown("---")  
st.markdown("""
<p style='text-align: center; color: black; font-size: 0.9rem;'>
Built with ❤️ By Uneeza Ismail | Stay safe, stay secure!
</p>
""", unsafe_allow_html=True)