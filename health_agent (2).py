# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nQyEtBo9x2J1oXy6LnYZnhCjkYFiF9OT
"""

from utils import alert

class HealthAgent:
    def __init__(self):
        self.thresholds = {
            'heart_rate': (60, 100),
            'blood_pressure': (90, 140),
            'spo2': 95
        }

    def process(self, df):
        for _, row in df.iterrows():
            if row['HeartRate'] < self.thresholds['heart_rate'][0] or row['HeartRate'] > self.thresholds['heart_rate'][1]:
                alert("Abnormal Heart Rate", row)

            if row['SystolicBP'] < self.thresholds['blood_pressure'][0] or row['SystolicBP'] > self.thresholds['blood_pressure'][1]:
                alert("Abnormal Blood Pressure", row)

            if row['SpO2'] < self.thresholds['spo2']:
                alert("Low Oxygen Saturation", row)