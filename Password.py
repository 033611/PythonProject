import streamlit as st
import re
import time
st.set_page_config("Password Strenght",page_icon="🔐")
# Function to check password strength
def check_password_strength(password):
    # Criteria for password strength
    length = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate strength score
    strength_score = sum([length, has_upper, has_lower, has_digit, has_special])

    # Determine strength level
    if strength_score == 5:
        return "Strong 💪", "green", "⭐⭐⭐"
    elif strength_score >= 3:
        return "Medium 😐", "orange", "⭐⭐"
    else:
        return "Weak 😢", "red", "⭐"

# Function to display password requirements checklist
def display_password_requirements(password):
    st.subheader("Password Requirements")
    requirements = {
        "At least 8 characters": len(password) >= 8,
        "Contains uppercase letters": bool(re.search(r'[A-Z]', password)),
        "Contains lowercase letters": bool(re.search(r'[a-z]', password)),
        "Contains numbers": bool(re.search(r'[0-9]', password)),
        "Contains special characters": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }
    for requirement, met in requirements.items():
        if met:
            st.markdown(f"✅ {requirement}")
        else:
            st.markdown(f"❌ {requirement}")

# Main app
def main():
    # Custom CSS to change font family
    st.markdown(
        """
        <style>
        h1 {
            font-family: serif;
        }
        body {
            font-family: serif;
        }
        .stButton > button {
            font-family: serif;
            background-color: #4A90E2;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
            transition: background-color 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #357ABD;
        }
        .stTextInput > div > input {
            font-family: serif;
            border-radius: 5px;
            border: 1px solid #4A90E2;
            padding: 10px;
            transition: border-color 0.3s ease;
        }
        .stTextInput > div > input:focus {
            border-color: #357ABD;
        }
        .stProgress > div > div > div {
            background-color: #4A90E2;
            border-radius: 5px;
            transition: width 0.5s ease;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.title("Password Strength Checker 🔐")
    st.write("Check the strength of your password with animations and emojis!")
  

    # Input field for password
    password = st.text_input("Enter your password:", type="password")

    # Check password strength button
    if st.button("Check Strength"):
        with st.spinner("Checking password strength..."):
            # Simulate a delay for animation
            progress_bar = st.progress(2)
            for i in range(100):
                time.sleep(0.01)  # Simulate a delay
                progress_bar.progress(i + 1)

            # Check password strength
            strength, color, stars = check_password_strength(password)

            # Display result with emojis and animations
            if strength == "Strong 💪":
                st.success(f"Password is {strength} {stars}")
                st.balloons()  # Celebrate with balloons
            elif strength == "Medium 😐":
                st.warning(f"Password is {strength} {stars}")
            else:
                st.error(f"Password is {strength} {stars}")

            # Display password requirements checklist
            display_password_requirements(password)

            # Change button background color dynamically
            st.markdown(
                f"""
                <style>
                div.stButton > button:first-child {{
                    background-color: {color};
                    color: white;
                    font-weight: bold;
                }}
                </style>
                """,
                unsafe_allow_html=True,
            )

if __name__ == "__main__":
    main()