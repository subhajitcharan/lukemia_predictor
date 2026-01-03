import streamlit as st
from extractor import processing
from prediction import make_Predictions
st.title("Lukemia Predictor")
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
def computation(upload):
    if upload is not None:
        st.image(upload)
        img_array=processing(uploaded_file)
        prediction,confidence=make_Predictions(img_array)
        return prediction,confidence
    else:
        st.write("no file added")

if uploaded_file is not None and st.button("submit"):
    prediction,confidence=computation(uploaded_file)
    st.write(f"prediction:{prediction}")
    st.write(f"confidence:{confidence*100}")
