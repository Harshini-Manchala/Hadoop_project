# Access Log Analysis using Hadoop, Hive & Isolation Forest

## Overview
This project analyzes web server access logs using Hadoop and Hive, converts processed results into CSV files, visualizes insights through a dashboard, and detects anomalies using Isolation Forest.

## Dataset
- Web server access logs (`access_logs`)
- Semi-structured text data (IP, timestamp, request, status code, size)
- Full dataset not included; a small sample file is provided

## Pipeline
access_logs → HDFS → Hive → CSV → Dashboard → Isolation Forest

## Technologies
- Apache Hadoop (HDFS)
- Apache Hive
- Python (Pandas, Scikit-learn)
- Streamlit (Dashboard)
- CSV files

## Folder Structure
- `mapreduce/` – Hadoop log processing code
- `analysis/` – Python scripts (visualization & anomaly detection)
- `data/` – Cleaned CSV files and sample logs

## Anomaly Detection
Isolation Forest is used to detect abnormal traffic patterns such as unusual request spikes or suspicious IP behavior.

## Run Dashboard
```bash
cd analysis
pip install pandas scikit-learn streamlit matplotlib
streamlit run streamlit_app.py
