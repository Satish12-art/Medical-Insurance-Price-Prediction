import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))


st.title("💰 Medical Insurance Cost Predictor")
st.write("Enter details to estimate insurance charges")

age = st.slider("Age", 18, 100)
# sex = st.selectbox("Select Gender", ["Male", "Female"],index=None,placeholder="Select Gender)
# if sex == "None":
#     st.warning("Please select a Gender ")
gender = st.selectbox(
    "Gender",
    ["Male", "Female"],
    index=None,
    placeholder="Select Gender"
)
region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"], index=None, placeholder="Select Region")
# if region == "None":
#     st.warning("Please select a region")
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0)
children = st.selectbox("Children", [0,1,2,3,4,5])
smoker = st.selectbox("Smoker", ["Yes", "No"])

smoker_val = 1 if smoker == "Yes" else 0
gender_val = 0 if gender == "Male" else 1
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0


# # Dummy region (simple version)
# region_northwest = 0
# region_southeast = 0
# region_southwest = 0

# Prediction
st.markdown("---")
if st.button("Predict"):
    input_data = np.array([[age, sex_val, bmi, children, smoker_val,
                            region_northwest, region_southeast, region_southwest]])

    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ₹ {prediction[0]:.2f}")


    st.subheader("About Model")
st.write("This model predicts insurance cost based on age, BMI, smoking habits, etc.")

