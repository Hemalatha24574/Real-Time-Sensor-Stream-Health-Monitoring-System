import threading
import time
import random
import json
from datetime import datetime

class SensorDevice(threading.Thread):
    def __init__(self, device_id, data_queue):
        threading.Thread.__init__(self)
        self.device_id = device_id
        self.queue = data_queue
        self.running = True
        self.msg_id = 0

    def generate_data(self):
        data = {
            "device_id": self.device_id,
            "temperature": round(random.uniform(60, 100), 2),
            "vibration": round(random.uniform(2, 15), 2),
            "voltage": round(random.uniform(150, 240), 2),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "message_id": self.msg_id
        }
        self.msg_id += 1
        return json.dumps(data)

    def run(self):
        while self.running:
            data = self.generate_data()
            self.queue.put(data)
            time.sleep(random.randint(1, 2))

    def stop(self):
        self.running = False
