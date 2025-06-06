import pandas as pd
import streamlit as st
import joblib

model = joblib.load('xgb_model.jb')

st.title('House Price Prediction')
st.write("Enter the Detail to find the price of te house")

input =['OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
       'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'Fireplaces',
       'BsmtFinSF1', 'LotFrontage', 'WoodDeckSF', 'OpenPorchSF', 'LotArea',
       'CentralAir']

input_data = {}
for features in input:
    if features == 'CentralAir':
        input[features] = st.selectbox(f"{features}", options=['Yes','No'], index=0)
    else:
        input_data[features]= st.number_input(
            f"{features}",
            value=0.0,
            step=1.0 if features in ['OverallQual','FullBath', 'FirePlaces']else 0.1
        )

if st.button("Predict Price"):
    input_data ['CentralAir'] =1 if  input_data ['CentralAir'] =="Yes" else 0

    input_df = pd.DataFrame([input_data],columns=input)

    predictions = model.predict(input_df)
    st.success (f"Predicted House Price: ${predictions[0]:,.2f}")

