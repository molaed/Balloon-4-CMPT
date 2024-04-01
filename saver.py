import csv
from datetime import datetime

class HelloTimestampLogger:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_hello_with_timestamp_to_csv(self):
        # Get the current timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # The message to be saved
        message = "Hello"

        # Open the file in append mode ('a') to add the new message with timestamp
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)

            # Write the message and timestamp to the file
            writer.writerow([message, timestamp])

        print(f"Message '{message}' with timestamp {timestamp} added to {self.file_path}")

# Example usage:
file_path = 'hello_timestamps.csv'
logger = HelloTimestampLogger(file_path)
logger.add_hello_with_timestamp_to_csv()

