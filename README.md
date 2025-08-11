# Flower Species Classifier (SVM + Flask)

This project is a web-based machine learning application that predicts the species of a flower (**Setosa**, **Versicolor**, or **Virginica**) using a Support Vector Machine (SVM) Classifier trained on the Iris dataset from `scikit-learn`.

The app provides a clean, user-friendly form that only requires 4 key flower features as input, each with example placeholder values for ease of use.

---

## 🚀 Features
- Predicts flower species using only 4 user-input numeric features
- SVM Classifier trained on the Iris dataset
- Responsive Flask web interface
- Example placeholders for user convenience

---

## 📂 Project Structure
flower-species-classifier/
│
├── app.py                  # Main Flask app
├── model.py                # Model training script
├── flower_svm_model.pkl    # Saved SVM classifier model
├── templates/
│   └── index.html          # Web interface template
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

---

## 📊 Dataset

Uses the **Iris Dataset** from scikit-learn, which contains measurements of iris flowers from three species:
- Setosa
- Versicolor
- Virginica

The web form collects these 4 features:
- Sepal Length (cm) *(e.g., 5.1)*
- Sepal Width (cm) *(e.g., 3.5)*
- Petal Length (cm) *(e.g., 1.4)*
- Petal Width (cm) *(e.g., 0.2)*

---

## 📦 Requirements
```
Flask
scikit-learn
pandas
numpy
joblib
```

Install all dependencies with:
```
pip install -r requirements.txt
```

---

## ▶️ Usage
1. Train the model (optional, model already included):
```
python model.py
```
2. Start the Flask app:
```
python app.py
```
3. Open your browser and go to:
```
http://127.0.0.1:5000
```

---
<<<<<<< HEAD

## 🖼️ Screenshot


=======
🖼 Screenshot
<img width="1366" height="640" alt="Screenshot 2025-08-11 001414" src="https://github.com/user-attachments/assets/0e99b875-0557-4a36-9006-8fb2824675cd" />
<img width="1366" height="633" alt="Screenshot 2025-08-11 001442" src="https://github.com/user-attachments/assets/4ed92198-6ac5-46b1-bf29-a0921fd04826" />
<img width="1366" height="633" alt="Screenshot 2025-08-11 001454" src="https://github.com/user-attachments/assets/dfad11ad-500d-420f-9ab2-5fe4f6d616f3" />
>>>>>>> c0b92cefbc4f0a7fec64805e965db6ccd270d26a
