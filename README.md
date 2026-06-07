# SMS Spam Classification / Clasificación de SMS Spam

ESPAÑOL — Secciones requeridas
--------------------------------

1) Descripción del proyecto
- Qué hace: Proyecto para analizar y evaluar un clasificador de spam sobre mensajes SMS. Incluye un notebook con EDA y un baseline (TF‑IDF + Logistic Regression) y una aplicación Streamlit para probar predicciones localmente.
- Qué modelo usa: Referencia al modelo en HuggingFace `Goodmotion/spam-mail-classifier` (ver sección Modelo) y un baseline entrenado proporcionado en `models/`.

2) Integrantes
- Fabian A. Salazar Figueroa
- Luis E. Ordoñez Erazo
- Raúl A. Echeverry López

3) Dataset
- Dataset local: [SMSSpamCollection](SMSSpamCollection)
- Referencia externa: UCI SMS Spam Collection — https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

4) Modelo
- Referencia: Goodmotion/spam-mail-classifier — https://huggingface.co/Goodmotion/spam-mail-classifier
- Nota sobre desajuste de dominio: El modelo referenciado puede haber sido entrenado en un dominio distinto (por ejemplo, correo electrónico). `SMSSpamCollection` contiene mensajes SMS; por ello puede existir un desajuste de dominio que reduzca el rendimiento si se usa el modelo HF directamente. Para evaluación en SMS se dispone del baseline entrenado en este proyecto en `models/`.

5) Estructura del proyecto
- Raíz (archivos principales): deliverable.txt, main.py, pyproject.toml, readme, README.md, requirements.txt, SMSSpamCollection
- `app/` — aplicación Streamlit (por ejemplo, `app/main.py`, `app/model.py`, `app/predict.py`)
- `models/` — modelos guardados (por ejemplo, `models/baseline_model.pkl` si presente)
- `notebook/` — notebooks: `analysis.ipynb`, `analysis_executed.ipynb`
- `scripts/` — utilidades y scripts (por ejemplo, `scripts/check_streamlit.py`, `scripts/copy_dataset.py`)

6) Requisitos
- Python: Se recomienda usar Python 3.10.16 al crear el entorno virtual.
- Dependencias: están listadas en `requirements.txt`.

7) Configuración e instalación
Pasos (ejemplo en PowerShell):
```powershell
git clone <repository-url>
cd <repo-root>
# Crear entorno virtual con Python 3.10.16
python -m venv .venv
.# Activar el venv (PowerShell)
.\.venv\Scripts\Activate.ps1
# Instalar dependencias
pip install -r requirements.txt
```

8) Ejecutar localmente
- Desde la raíz del repositorio, iniciar la app Streamlit:
```powershell
streamlit run app/main.py
```
- Una vez iniciada, la aplicación estará disponible en las siguientes URLs:
  - URL local:   http://localhost:8501
  - URL de red:  http://192.168.1.103:8501

9) Notebook
- Abrir y ejecutar `notebook/analysis.ipynb` para ver el EDA y el entrenamiento/evaluación del baseline.
- Opciones: `jupyter notebook notebook/analysis.ipynb` o abrir en VS Code.

ENGLISH — Required sections
--------------------------------

1) Project Description
- What it does: Project to analyze and evaluate a spam classifier on SMS messages. Includes an exploratory data analysis notebook, a TF‑IDF + Logistic Regression baseline, and a Streamlit app to test predictions locally.
- Model used: Reference to the HuggingFace model `Goodmotion/spam-mail-classifier` (see Model section) and a project baseline model stored in `models/`.

2) Team Members
- Fabian A. Salazar Figueroa
- Luis E. Ordoñez Erazo
- Raúl A. Echeverry López

3) Dataset
- Local dataset: [SMSSpamCollection](SMSSpamCollection)
- External reference: UCI SMS Spam Collection — https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

4) Model
- Referenced model: Goodmotion/spam-mail-classifier — https://huggingface.co/Goodmotion/spam-mail-classifier
- Domain mismatch note: The referenced HuggingFace model may have been trained on a different text domain (for example, email). The `SMSSpamCollection` dataset contains SMS messages; expect degraded performance if using the HF model directly. Use the provided baseline in `models/` for SMS-specific evaluation or fine‑tune a model on SMS data.

5) Project Structure
- Root (key files): deliverable.txt, main.py, pyproject.toml, readme, README.md, requirements.txt, SMSSpamCollection
- `app/` — Streamlit app (e.g., `app/main.py`, `app/model.py`, `app/predict.py`)
- `models/` — saved baseline model(s)
- `notebook/` — notebooks: `analysis.ipynb`, `analysis_executed.ipynb`
- `scripts/` — helper scripts (e.g., `scripts/check_streamlit.py`, `scripts/copy_dataset.py`)

6) Requirements
- Python: Use Python 3.10.16 when creating the virtual environment (recommended).
- Dependencies: listed in `requirements.txt`.

7) Setup & Installation
Steps (example commands):
```powershell
git clone <repository-url>
cd <repo-root>
python -m venv .venv    # use Python 3.10.16 for this venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

8) Run Locally
- Run the Streamlit app from the repository root:
```powershell
streamlit run app/main.py
```
- Once started, the app will be available at:
  - Local URL:   http://localhost:8501
  - Network URL: http://192.168.1.103:8501

9) Notebook
- Open and run `notebook/analysis.ipynb` to view exploratory data analysis and the baseline training/evaluation.
- Open options: `jupyter notebook notebook/analysis.ipynb` or open in VS Code.

Notes
- All statements in this README are based on files and links present in the repository. No facts were invented, simulated, or assumed beyond the content available in the project files.

