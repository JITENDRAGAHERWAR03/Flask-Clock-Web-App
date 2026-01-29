# 🕒 Flask Clock Web App

A modern and minimal **web-based clock application** built using **Flask**, **HTML**, **CSS**, and **JavaScript**.  
It displays a beautiful **analog clock** along with a **real-time digital clock**, and also provides a backend API to fetch UTC time data.

This project is perfect for beginners who want to understand how frontend and backend work together in a Python web app.

---

## 🚀 Features

- 🕰 Real-time **Analog Clock**
- ⏱ Live **Digital Time Display**
- 🌐 Flask backend with API endpoint
- 📡 Fetches UTC time from WorldTimeAPI 
- 🎨 Modern UI with gradient background 
- ⚡ Pure JavaScript clock animation 

---

## 🗂 Project Structure
```
Flask-Clock-App/
│
├── app.py
├── requirements.txt
│
├── templates/
│ └── index.html
│
└── static/
├── styles.css
└── script.js
```
---
- `app.py` – Flask server & API   
- `index.html` – Main UI layout   
- `styles.css` – Styling & clock design   
- `script.js` – Clock logic & animation   

---

## 🛠 Installation & Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/flask-clock-app.git
cd flask-clock-app
```
---
2.Install dependencies:
```
pip install -r requirements.txt
```

3.Run the app:
```
python app.py
```

4.Open in browser:
```
http://127.0.0.1:5000/
```
---
🔌 API Endpoint

You can also fetch UTC time from:

GET /api/time


Example response:

{
  "utc_time": "2026-01-29T15:42:10+00:00",
  "timezone": "Etc/UTC",
  "day_of_week": "Thursday",
  "day_of_year": "029"
}

📸 Preview

Add a screenshot or GIF here:

![Clock Preview](preview.png)


You can create a GIF using tools like:

ScreenToGif (Windows)

OBS Studio

LICEcap

💡 Learning Outcomes

Flask routing & API creation

Frontend–Backend integration

JavaScript DOM manipulation

CSS positioning & transforms

Real-time UI updates

👨‍💻 Author

Jitendra KanhaiyaSingh Gaherwar
B.Tech IT | Data & AI Developer
Focused on building practical projects with Python & AI.
