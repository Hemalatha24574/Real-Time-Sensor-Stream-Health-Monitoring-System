import json
import logging
from datetime import datetime
import os

class DataProcessor:
    def __init__(self, db):
        self.db = db
        self.device_stats = {}

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logging.basicConfig(
            filename="logs/alerts.log",
            level=logging.WARNING,
            format="%(asctime)s - %(message)s"
        )

        self.critical_logger = logging.getLogger("critical")
        handler = logging.FileHandler("logs/critical_alerts.log")
        self.critical_logger.addHandler(handler)

    def process(self, raw_data):
        data = json.loads(raw_data)
        device = data["device_id"]

        if device not in self.device_stats:
            self.device_stats[device] = {
                "packets": 0,
                "errors": 0,
                "start_time": datetime.now(),
                "last_active": None
            }

        self.device_stats[device]["packets"] += 1
        self.device_stats[device]["last_active"] = datetime.now()

        # -------- NEW HEALTH SCORE LOGIC --------
        health_score = 100
        alert_type = "None"

        if data["temperature"] > 80:
            health_score -= 30
            alert_type = "Temperature Risk"

        if data["vibration"] > 8:
            health_score -= 25
            alert_type = "Vibration Risk"

        if data["voltage"] < 190:
            health_score -= 20
            alert_type = "Voltage Risk"

        if health_score >= 70:
            status = "Good"
        elif health_score >= 40:
            status = "Warning"
        else:
            status = "Critical"

        # -------- ALERT HANDLING --------
        if status == "Warning":
            logging.warning(f"{device} - Score {health_score} " + "Warning sent")
            print(f"[WARNING] {device} health dropping ({health_score}) " + "Warning sent")
            print("EMAIL: Warning sent")

        if status == "Critical":
            self.critical_logger.critical(f"{device} - Score {health_score} "+ "CRITICAL sent")
            print(f"[CRITICAL] {device} unhealthy ({health_score})" +" " + "CRITICAL sent")
            print("EMAIL: CRITICAL sent")
            self.device_stats[device]["errors"] += 1

        data["status"] = status
        data["alert_type"] = alert_type
        data["health_score"] = health_score

        self.db.insert(data)
        return data
