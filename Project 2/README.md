# Car Evaluation Classification API

A Machine Learning web application built using **FastAPI** and **Random Forest Classifier** that predicts the evaluation category of a car based on its specifications.

This project was developed as **Project 2** for the **DecodeLabs AI Internship**.

---

## Features

- Predicts car evaluation category
- FastAPI backend
- HTML & CSS frontend
- Random Forest machine learning model
- Trained on the Car Evaluation Dataset
- Responsive web interface
- REST API support

---

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas
- Joblib
- HTML
- CSS
- Jinja2
- Uvicorn

---

## Dataset

**Car Evaluation Dataset**

The dataset contains information about different car attributes:

- Buying Price
- Maintenance Cost
- Number of Doors
- Passenger Capacity
- Luggage Boot Size
- Safety Rating

Target Classes:

- Unacceptable (unacc)
- Acceptable (acc)
- Good (good)
- Very Good (vgood)

---

## Machine Learning Model

Algorithm:

- Random Forest Classifier

Accuracy:

- 97%

Evaluation Metrics:

- Accuracy Score
- Classification Report

---

## Project Structure

```
Car-Evaluation-API
│
├── dataset/
│   └── car.csv
│
├── model/
│   ├── car_model.pkl
│   └── label_encoders.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── train_model.py
├── predictor.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd Car-Evaluation-API
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn main:app --reload
```

Open your browser

```
http://127.0.0.1:8000
```

---

## API Endpoint

### Home

```
GET /
```

Displays the web application.

---

## Prediction


Input Parameters

- Buying Price
- Maintenance Cost
- Doors
- Persons
- Luggage Boot
- Safety

Output

```
Very Good
Good
Acceptable
Unacceptable
```

---

## Example Prediction

| Feature | Value |
|----------|-------|
| Buying | Low |
| Maintenance | Low |
| Doors | 4 |
| Persons | More |
| Luggage | Big |
| Safety | High |

Prediction

```
Very Good
```

---

## Future Improvements

- Prediction confidence score
- Model comparison
- User authentication
- Database integration
- Docker deployment
- Cloud deployment
- Interactive dashboard

---

## Author

**Sabeeh Waheed**

BS Computer Science  
AI & Machine Learning Enthusiast

---

## Internship

Developed as part of the **DecodeLabs AI Internship**.