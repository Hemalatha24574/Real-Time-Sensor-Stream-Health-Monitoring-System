# 🔧 Real-Time Sensor Data Stream Processor & Device Health Monitoring System

## 📌 Overview
This project is a **Python-based real-time monitoring system** that simulates sensor data streams from multiple devices, processes them live, detects anomalies, tracks device health, logs alerts, and generates daily reports.

It mimics real-world **industrial IoT monitoring systems** used in:
- Factories
- Warehouses
- Robotics & automation
- Logistics and smart infrastructure

---

## 🎯 Features
✔ Multi-threaded sensor data simulation  
✔ Real-time JSON data processing  
✔ Threshold-based anomaly detection  
✔ Device health scoring & status tracking  
✔ Warning & critical alert logging  
✔ Email alert simulation (console output)  
✔ SQLite-based persistent storage  
✔ Automatic daily report generation  

---

## 📂 Project Folder Structure
```
sensor_monitor/
│── sensors/
│   └── sensor_simulator.py
│
│── processor/
│   └── data_processor.py
│
│── storage/
│   └── database.py
│
│── reports/
│   └── report_generator.py
│
│── logs/
│   ├── alerts.log
│   └── critical_alerts.log
│
│── main.py
│── README.md
```

---

## 🔄 System Workflow
1. **Sensor Simulation**
   - Multiple devices run as threads
   - Each sends temperature, vibration & voltage every 1–2 seconds

2. **Data Processing**
   - JSON data validated & analyzed
   - Health score calculated
   - Status assigned: `Good / Warning / Critical`

3. **Alerting**
   - Warnings → `alerts.log`
   - Critical → `critical_alerts.log`
   - Console + email simulation

4. **Storage**
   - All processed data stored in SQLite database

5. **Reporting**
   - Auto-generated daily report every 60 seconds
   - Saved as `report_<date>.txt`

---

## ⚠ Threshold Rules
| Metric | Condition | Action |
|------|---------|--------|
| Temperature | > 80°C | Risk |
| Vibration | > 8.0 | Risk |
| Voltage | < 190V | Risk |

Health score determines device status.

---

## 🛠 Technologies Used
- Python 3.x
- threading
- queue
- sqlite3
- logging
- random
- datetime

---

## ▶ How to Run
```bash
python main.py
```

Press **CTRL + C** to stop the system.

---

## 📊 Sample Output
```
[WARNING] Device_2 health dropping (55)
[CRITICAL] Device_3 unhealthy (30)
EMAIL: CRITICAL sent
```

---

## 📄 Generated Files
- `sensor_data.db` → SQLite database
- `alerts.log` → Warning alerts
- `critical_alerts.log` → Critical alerts
- `reports/report_YYYY-MM-DD.txt`

---

## 🚀 Future Enhancements
- PDF report generation
- Real email integration
- Web dashboard
- REST API
- Cloud database support

---

## 👨‍💻 Author
Developed for **Real-Time Systems & Python Projects**  
Perfect for **academic projects, interviews, and IoT demos**
