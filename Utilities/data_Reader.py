import csv
import configparser
import os
from pathlib import Path

class DataReader:
    @staticmethod
    def read_csv(file_path):
        test_data = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                test_data.append(row)
        return test_data




