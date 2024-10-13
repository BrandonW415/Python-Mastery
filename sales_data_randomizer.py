import csv
import random
import time
import shutil
import os
import logging
from datetime import datetime, timedelta

logging.basicConfig(filename='csv_shuffler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CSVShuffler:
    def __init__(self, input_file, backup_dir, interval_seconds=10):
        self.input_file = input_file
        self.backup_dir = backup_dir
        self.interval_seconds = interval_seconds
        self.last_backup_date = None
        
    def read_csv(self):
        try:
            with open(self.input_file, 'r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader)
                data = list(reader)
            return header, data
        except Exception as e:
            logging.error(f"Error reading CSV file: {e}")
            return None, None
        
    def write_csv(self, header, data):
        try:
            with open(self.input_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(data)
            logging.info(f"CSV file shuffled and written: {self.input_file}")
        except Exception as e:
            logging.error(f"Error writing CSV file: {e}")
            
    def backup_file(self):
        today = datetime.now().date()
        if self.last_backup_date != today:
            try:
                backup_file = os.path.join(self.backup_dir, f"backip_{today.strftime('%Y%m%d')}_{os.path.basename(self.input_file)}")
                shutil.copy2(self.input_file, backup_file)
                self.last_backup_date = today
                logging.info(f"Backup created: {backup_file}")
            except Exception as e:
                logging.error(f"Error creating backup: {e}")
                
    def shuffle_and_backup(self):
        self.backup_file()
        header, data = self.read_csv()
        if header and data:
            random.shuffle(data)
            self.write_csv(header, data)
            
    def run(self):
        while True:
            self.shuffle_and_backup()
            time.sleep(self.interval_seconds)
            
if __name__ == "__main__":
    input_file = "./sales_data.csv"
    backup_dir = "backups"
    interval_seconds = 10 # Set to 86400 seconds if you want to have daily shuffling
    os.makedirs(backup_dir, exist_ok=True)
    shuffler = CSVShuffler(input_file, backup_dir, interval_seconds)
    logging.info("Start CSV Shuffler")
    try:
        shuffler.run()
    except KeyboardInterrupt:
        logging.info("CSV Suffler stopeed by user")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")