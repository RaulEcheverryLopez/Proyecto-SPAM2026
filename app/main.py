import streamlit as st
from model import load_model, predict_text

st.set_page_config(page_title="SMS Spam Demo", layout="centered")

st.title("SMS Spam Detection — Demo")

st.markdown("Enter an SMS message below and press Predict.")

model, tokenizer = load_model()

text = st.text_area("SMS text", height=150)

if st.button("Predict"):
    if not text.strip():
        st.warning("Please enter a message to classify.")
    else:
        label, score = predict_text(model, tokenizer, text)
        st.write("**Prediction:**", label)
        st.write("**Confidence:** {:.2%}".format(score))

st.markdown("---")
st.markdown("### Example from dataset")
try:
    with open('SMSSpamCollection','r',encoding='utf-8') as f:
        sample = f.readline().strip()
    st.write(sample)
except Exception:
    st.write("Dataset file not found in repository root. Run `python scripts/copy_dataset.py` to prepare data.")
