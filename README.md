# 🌸 Flower Species Classifier (SVM + Flask)

This project is a web-based machine learning application that predicts the species of a flower (Setosa, Versicolor, or Virginica) using a Support Vector Machine (SVM) Classifier trained on the Iris dataset from scikit-learn.

The app provides a clean, user-friendly form that only requires 4 key flower features as input, each with example placeholder values for ease of use.

---

## 🚀 Features

- Predicts flower species using only 4 numeric input features
- SVM Classifier trained on the Iris dataset
- Responsive Flask web interface
- Example placeholders in input fields for user convenience

---

## 📂 Project Structure

```
flower-species-classifier/
│
├── app.py                   # Main Flask application
├── model.py                 # Model training script
├── flower_svm_model.pkl     # Saved SVM classifier model
├── requirements.txt         # Python dependencies
├── templates/
│   └── index.html           # Web interface template
└── README.md                # Project documentation
```

---

## 📊 Dataset

This project uses the famous Iris Dataset from scikit-learn, which contains measurements of iris flowers from three species:

- Setosa
- Versicolor
- Virginica

The web form collects these 4 features as input:

| Feature           | Example Value |
|-------------------|---------------|
| Sepal Length (cm) | 5.1           |
| Sepal Width (cm)  | 3.5           |
| Petal Length (cm) | 1.4           |
| Petal Width (cm)  | 0.2           |

---

## 📦 Requirements

- Python 3.x
- Flask
- scikit-learn
- pandas
- numpy
- joblib

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1. **Train the model (optional, since model file is included):**

```bash
python model.py
```

2. **Run the Flask app:**

```bash
python app.py
```

3. **Open your browser and go to:**

```
http://127.0.0.1:5000
```

---

## 🖼️ Screenshot

<img width="1366" height="640" alt="Screenshot 2025-08-11 001414" src="https://github.com/user-attachments/assets/ea4a9e73-65fa-428f-83b3-912061b04d98" />
<img width="1366" height="633" alt="Screenshot 2025-08-11 001442" src="https://github.com/user-attachments/assets/c10a5782-ce7f-4ede-809c-0001f4eed6ad" />
<img width="1366" height="633" alt="Screenshot 2025-08-11 001454" src="https://github.com/user-attachments/assets/db47e299-fd74-456e-8fa7-ca098461687d" />


---


