import streamlit as st
import time
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Unit Converter", page_icon="📊", layout="centered")

# Title with emojis
st.title("Unit Converter 📊")
st.write("**Convert between different units dynamically with animations and graphs!**")

# Conversion functions
def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        "kg": 1.0,
        "g": 1000.0,
        "mg": 1e6,
        "lb": 2.20462,
        "oz": 35.274
    }
    return value * (weight_conversions[to_unit] / weight_conversions[from_unit])

def convert_length(value, from_unit, to_unit):
    length_conversions = {
        "m": 1.0,
        "cm": 100.0,
        "mm": 1000.0,
        "km": 0.001,
        "in": 39.3701,
        "ft": 3.28084,
        "yd": 1.09361,
        "mi": 0.000621371
    }
    return value * (length_conversions[to_unit] / length_conversions[from_unit])

def convert_time(value, from_unit, to_unit):
    time_conversions = {
        "s": 1.0,
        "min": 1 / 60,
        "hr": 1 / 3600,
        "day": 1 / 86400,
        "week": 1 / 604800,
        "year": 1 / 31536000
    }
    return value * (time_conversions[to_unit] / time_conversions[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C":
        if to_unit == "F":
            return (value * 9/5) + 32
        elif to_unit == "K":
            return value + 273.15
        else:
            return value
    elif from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5/9
        elif to_unit == "K":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "K":
        if to_unit == "C":
            return value - 273.15
        elif to_unit == "F":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value

# Function to plot dynamic graph
def plot_dynamic_graph(input_value, output_value, input_unit, output_unit):
    fig, ax = plt.subplots()
    ax.bar([input_unit, output_unit], [input_value, output_value], color=["blue", "green"])
    ax.set_ylabel("Value")
    ax.set_title("Conversion Comparison 📊")
    st.pyplot(fig)

# Main app
def main():
    # Select conversion type with emojis
    conversion_type = st.selectbox(
        "**Select Conversion Type:**",
        ["⚖️ Weight", "📏 Length", "⏰ Time", "🌡️ Temperature"],
        help="Choose the type of unit you want to convert."
    )

    # Remove emojis for internal logic
    conversion_type = conversion_type.split(" ")[1]  # Extract "Weight", "Length", etc.

    # Dynamic unit selection based on conversion type
    if conversion_type == "Weight":
        units = ["kg", "g", "mg", "lb", "oz"]
    elif conversion_type == "Length":
        units = ["m", "cm", "mm", "km", "in", "ft", "yd", "mi"]
    elif conversion_type == "Time":
        units = ["s", "min", "hr", "day", "week", "year"]
    elif conversion_type == "Temperature":
        units = ["C", "F", "K"]

    # Input fields
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("**From:**", units, help="Select the unit to convert from.")
    with col2:
        to_unit = st.selectbox("**To:**", units, help="Select the unit to convert to.")

    value = st.number_input(f"**Enter value in {from_unit}:**", value=1.0, help="Enter the value you want to convert.")

    # Dynamic button text with emojis
    button_text = f"✨ Convert {from_unit} to {to_unit} ✨"

    # Convert button with animation
    if st.button(button_text, help="Click to perform the conversion."):
        with st.spinner("🔮 Converting..."):
            # Progress bar animation
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.02)  # Simulate a delay
                progress_bar.progress(i + 1)

            # Perform conversion
            if conversion_type == "Weight":
                result = convert_weight(value, from_unit, to_unit)
            elif conversion_type == "Length":
                result = convert_length(value, from_unit, to_unit)
            elif conversion_type == "Time":
                result = convert_time(value, from_unit, to_unit)
            elif conversion_type == "Temperature":
                result = convert_temperature(value, from_unit, to_unit)

            # Display result with emojis
            st.success(f"✅ Converted value: **{result:.2f} {to_unit}**")

            # Plot dynamic graph
            plot_dynamic_graph(value, result, from_unit, to_unit)

# Run the app
if __name__ == "__main__":
    main()