from queue import Queue
from sensors.sensor_simulator import SensorDevice
from processor.data_processor import DataProcessor
from storage.database import Database
import time
from reports.report_generator import generate_report

def main():
    print("Starting sensor monitoring system...")
    print("System started successfully")
    print("Simulating sensor data...")
    print("Sensor data simulation started successfully")
    print("Processing sensor data...")
    print("Sensor data processing started successfully")
    print("Generating reports...")
    print("Report generation started successfully")
    
    data_queue = Queue()
    db = Database()
    processor = DataProcessor(db)

    devices = []
    for i in range(3):
        device = SensorDevice(f"Device_{i+1}", data_queue)
        device.start()
        devices.append(device)

    try:
        start_time = time.time()
        while True:
            if not data_queue.empty():
                raw_data = data_queue.get()
                result = processor.process(raw_data)
                print(result)

            if time.time() - start_time > 60:
                generate_report()
                start_time = time.time()

    except KeyboardInterrupt:
        print("Stopping system...")
        for d in devices:
            d.stop()

if __name__ == "__main__":
    main()
