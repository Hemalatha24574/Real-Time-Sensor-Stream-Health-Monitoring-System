import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("sensor_data.db", check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS sensor_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT,
            temperature REAL,
            vibration REAL,
            voltage REAL,
            health_score INTEGER,
            status TEXT,
            alert_type TEXT,
            timestamp TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert(self, data):
        query = """
        INSERT INTO sensor_logs 
        (device_id, temperature, vibration, voltage, health_score, status, alert_type, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        values = (
            data["device_id"],
            data["temperature"],
            data["vibration"],
            data["voltage"],
            data["health_score"],
            data["status"],
            data["alert_type"],
            data["timestamp"]
        )
        self.conn.execute(query, values)
        self.conn.commit()

