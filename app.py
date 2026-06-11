import streamlit as st
import pickle
import numpy as np

loaded_model = pickle.load(open('rock_vs_mine_model.pkl', 'rb'))

st.title("Rock vs Mine Prediction")
input_data = st.text_area("Enter 60 values separated by commas")

if st.button("Predict"):
    try:
        values = [float(x.strip()) for x in input_data.split(",")]

        st.write("Number of values:", len(values))

        if len(values) != 60:
            st.error(f"Please enter exactly 60 values. You entered {len(values)} values.")
        else:
            prediction = loaded_model.predict([values])

            if prediction[0] == "R":
                st.success("Rock")
            else:
                st.success("Mine")

    except ValueError:
        st.error("Please enter only numeric values separated by commas.")
