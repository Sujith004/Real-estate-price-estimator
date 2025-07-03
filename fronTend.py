import streamlit as st
import pandas as pd
import joblib
model=joblib.load("gradient_boost_model.pkl")
st.title("🏡 Real Estate Price Estimator🏡")
st.subheader("Enter House details to predict the price ")
bedrooms=st.number_input("Enter the number of bedrooms ",min_value=0,step=1)
bathrooms=st.number_input("Enter the number of bathroom ",min_value=0.0,step=0.25)
sqft_living=st.number_input("Living area (in sqft) ",min_value=0)
sq_lot=st.number_input("Total area (in sqft) ",min_value=0)
floors=st.number_input("Number of Floors ",min_value=1.0,max_value=3.5,step=0.5)
waterfront=st.radio("Waterfront property? ",["No","Yes"])
view=st.selectbox("View quality from the house (0,4) ",[0,1,2,3,4])
condition=st.selectbox("Condition (1-5) ",[1,2,3,4,5])
grade=st.selectbox("Construction grade (1-13)" ,list(range(1,14)))
sqft_above=st.number_input("Area above ground level (in sqft) ",min_value=0)
sqft_basement=st.number_input("Basement area (in sqft) ",min_value=0)
yr_build=st.number_input("House build year ",min_value=1900,max_value=2025)
# yr_renovated = st.number_input("Year of renovation (0 if never renovated)", min_value=0, max_value=2025)
use_custom_location=st.checkbox("Customized latitude and longitude?")
if use_custom_location:
    latitude = st.number_input("Enter latitude",format="%.6f",value=47.5112)
    longitude=st.number_input("Enter longitude",format="%.6f",value=-122.257)
else:
    latitude = 47.5112
    longitude = -122.257
waterfront_val=1 if waterfront=="Yes" else 0
# renovated_val=1 if renovated=="Yes"else 0
input_data=pd.DataFrame([{
    'bedrooms':bedrooms,
    'bathrooms':bathrooms,
    'sqft_living':sqft_living,
    'sqft_lot':sq_lot,
    'floors':floors,
    'waterfront':waterfront_val,
    'view':view,
    'condition':condition,
    'grade':grade,
    'sqft_above':sqft_above,
    'sqft_basement':sqft_basement,
    'yr_built':yr_build,
    # 'yr_renovated': yr_renovated,
    'lat':latitude,
    'long':longitude
}])
if st.button("Predicted Price"):
    try:
        prediction=model.predict(input_data)[0]
        st.success(f"Estimated House Price: ${prediction:,.0f}")
    except Exception as e:
        st.error(f"⚠ Error during Prediction: {e}")