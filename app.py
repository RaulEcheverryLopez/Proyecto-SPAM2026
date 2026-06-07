from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


DATA_PATH = Path(__file__).resolve().parent / "data" / "sms_spam_sample.csv"


@st.cache_resource
def train_model() -> Pipeline:
    data = pd.read_csv(DATA_PATH)
    model = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2))),
            ("clf", LogisticRegression(max_iter=1000, random_state=42)),
        ]
    )
    model.fit(data["text"], data["label"])
    return model


def predict_message(message: str) -> tuple[str, float]:
    model = train_model()
    predicted_label = model.predict([message])[0]
    confidence = float(model.predict_proba([message]).max())
    return predicted_label, confidence


def main() -> None:
    st.set_page_config(page_title="Clasificador SMS Spam", page_icon="📩")
    st.title("Clasificador de Spam en SMS")
    st.write("Baseline: TF‑IDF + Logistic Regression")

    user_message = st.text_area("Escribe un mensaje SMS para clasificar:", height=120)

    if st.button("Predecir", type="primary"):
        if not user_message.strip():
            st.warning("Por favor escribe un mensaje antes de predecir.")
            return

        label, confidence = predict_message(user_message.strip())
        if label == "spam":
            st.error(f"Predicción: **SPAM** (confianza: {confidence:.2%})")
        else:
            st.success(f"Predicción: **HAM** (confianza: {confidence:.2%})")


if __name__ == "__main__":
    main()
