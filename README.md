# Proyecto-SPAM2026
Proyecto para analizar y evaluar un clasificador de spam sobre mensajes SMS. Incluye un notebook con EDA y un baseline (TF‑IDF + Logistic Regression) y una aplicación Streamlit para probar predicciones localmente.

## Estructura

- `/data/sms_spam_sample.csv`: muestra de mensajes SMS etiquetados (`ham`/`spam`).
- `/notebooks/eda_baseline_sms_spam.ipynb`: EDA y baseline con TF‑IDF + Logistic Regression.
- `/app.py`: aplicación Streamlit para predicción local.

## Uso rápido

1. Instalar dependencias:
   - `pip install -r requirements.txt`
2. Abrir notebook:
   - `jupyter notebook /tmp/workspace/RaulEcheverryLopez/Proyecto-SPAM2026/notebooks/eda_baseline_sms_spam.ipynb`
3. Ejecutar app Streamlit:
   - `streamlit run /tmp/workspace/RaulEcheverryLopez/Proyecto-SPAM2026/app.py`
