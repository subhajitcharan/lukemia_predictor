import streamlit as st
from src.extractor import processing
from src.prediction import make_Predictions
st.title("Lukemia Predictor(Blood Cancer Detector)")
st.warning("Warning:Only for Educational Purposes.Use peripheral blood smear (PBS) for testing")
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
def computation(upload):
    st.image(upload)
    img_array=processing(upload)
    prediction,confidence=make_Predictions(img_array)
    return prediction,confidence
    

if  st.button("submit"):
    if uploaded_file is not None:
        prediction,confidence=computation(uploaded_file)
        st.write(f"prediction:{prediction}")
        st.write(f"confidence:{confidence*100}")
    else:
        st.write("no file found")
