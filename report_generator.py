import sqlite3
from datetime import date
import os

def generate_report():
    conn = sqlite3.connect("sensor_data.db")
    cursor = conn.cursor()

    today = date.today().strftime("%Y-%m-%d")

    cursor.execute("SELECT COUNT(*) FROM sensor_logs")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM sensor_logs WHERE status='Critical'")
    critical = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(health_score) FROM sensor_logs")
    avg_score = cursor.fetchone()[0]

    cursor.execute("SELECT device_id, COUNT(*) FROM sensor_logs GROUP BY device_id")
    device_list = cursor.fetchall()

    report = f"""
DEVICE HEALTH REPORT - {today}

Total Data Packets: {total}
Critical Devices Count: {critical}
Average Health Score: {round(avg_score,2)}

Device Activity:
"""

    for d in device_list:
        report += f"{d[0]} → {d[1]} packets\n"



    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/report_{today}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)

    print("Report created:", filename)
