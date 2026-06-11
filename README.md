#  Rock vs Mine Prediction App

A Machine Learning web application that predicts whether a sonar signal is reflected from a **Rock** or a **Mine**.

##  Live Demo

 Live App: https://rock-vs-mine-chan.streamlit.app/

## Project Overview

This project uses a Machine Learning classification model trained on the Sonar dataset. Users can enter 60 sonar feature values, and the model predicts whether the object is:

-  Rock (R)
-  Mine (M)

The application is built using Streamlit and deployed on Streamlit Community Cloud. Streamlit allows Python-based data applications to be deployed and shared easily. :contentReference[oaicite:0]{index=0}

##  Technologies Used

- Python
- NumPy
- Pandas
- Scikit-Learn
- Streamlit

##  Project Structure

```text
rockVSmine/
│
├── app.py
├── sonar_model.pkl
├── sonar_data.csv
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/chandrika018/rockVSmine.git
cd rockVSmine
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

Streamlit runs Python scripts as interactive web applications. :contentReference[oaicite:1]{index=1}

##  Dataset

The project uses the Sonar Dataset, which contains 60 numerical attributes representing sonar signal returns and a target label:

- R = Rock
- M = Mine

##  Features

- User-friendly web interface
- Real-time prediction
- Machine Learning classification
- Streamlit deployment
- Easy to use and lightweight

## 📷 Application Screenshot

Add a screenshot of your deployed application here.

##  Future Improvements

- Better UI/UX
- Input validation
- Probability score display
- Model performance visualization
- Batch prediction support

##  Author

**Chandrika Nandehariya**

GitHub: https://github.com/chandrika018
