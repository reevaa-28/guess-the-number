import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter Weight (kg)", min_value=1.0, value=50.0)
height = st.number_input("Enter Height (m)", min_value=0.1, value=1.70)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)

    st.write(f"Weight: {weight} kg")
    st.write(f"Height: {height} m")
    st.success(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.info("Category: Underweight")
    elif bmi < 25:
        st.success("Category: Normal Weight")
    elif bmi < 30:
        st.warning("Category: Overweight")
    else:
        st.error("Category: Obese")