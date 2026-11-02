# Smart AI Adaptive Traffic Control System

## 1. Project Overview

The **Smart AI Adaptive Traffic Control System** is a data-driven traffic monitoring and analytics project designed to analyze traffic conditions across different areas of Bengaluru.

The project uses historical traffic data to analyze traffic volume, average vehicle speed, congestion patterns, and traffic situations. Python is used for data cleaning, analysis, and visualization, while Power BI provides an interactive dashboard.

## 2. Problem Statement

Traffic congestion is a major challenge in urban areas like Bengaluru. Traffic conditions vary depending on location, time of day, traffic volume, road capacity, and other factors.

This project aims to analyze traffic data and provide useful insights that support better traffic monitoring and traffic management decisions.

## 3. Project Objectives

- Analyze historical traffic data.
- Identify high, medium, and low traffic conditions.
- Analyze area-wise traffic volume.
- Study average vehicle speed and congestion patterns.
- Visualize traffic trends over time.
- Develop an interactive Power BI dashboard.
- Support data-driven traffic management decisions.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Power BI | Interactive dashboard |
| GitHub | Version control and collaboration |

## 5. Dataset Description

The project uses the **Bengaluru Traffic 2023–2024 dataset** obtained from Kaggle.

**Dataset source:** [Bengaluru Traffic 2023–2024](https://www.kaggle.com/datasets/sandheepkochi/bangalore-traffic-2023-2024)

Important dataset columns include:

- Date
- Area Name
- Road/Intersection Name
- Traffic Volume
- Average Speed
- Travel Time Index
- Congestion Level
- Incident Reports
- Weather Conditions
- TimeBlock
- TrafficSituation

## 6. Project Modules

### Module 1: Data Collection
Collection and organization of Bengaluru traffic data for analysis.

### Module 2: Data Cleaning
Handling missing values, duplicate records, invalid values, and data formatting.

### Module 3: Data Analysis
Analyzing traffic volume, average speed, traffic situations, and time-based traffic patterns.

### Module 4: Data Visualization
Creating Python visualizations to understand traffic conditions and identify patterns.

### Module 5: Interactive Dashboard
Developing a Power BI dashboard with KPI cards, charts, and interactive slicers.

## 7. Power BI Dashboard Features

The interactive dashboard contains **6 KPI cards**:

1. Total Traffic Records
2. Areas Monitored
3. Average Speed
4. High Traffic Records
5. Medium Traffic Situation
6. Low Traffic Situation

### Dashboard Visualizations

1. Average Traffic Volume by Area
2. Traffic Situation Distribution
3. Monthly Traffic Volume Trend Over Time
4. Traffic Volume vs Average Speed
5. Congestion by Area

### Interactive Slicers

- Area Name
- TrafficSituation
- Date
- TimeBlock

Users can select different filters to explore traffic patterns and compare traffic conditions.

## 8. Project Folder Structure

```text
Smart-AI-Adaptive-Traffic-Control/
│
├── visualizations/
├── bangalore_traffic_cleaned.csv
├── bangalore_traffic_timely_data.csv
├── data_cleaning.py
├── data_analysis.py
├── data_visualization.py
├── data_collection.md
├── data_cleaning_report.md
├── data_analysis_report.md
├── data_visualization_report.md
├── project_proposal.md
├── traffic_volume_by_area.csv
├── average_speed_by_area.csv
├── traffic_situation_counts.csv
├── traffic_volume_by_timeblock.csv
├── average_speed_by_timeblock.csv
├── traffic_situations_by_timeblock.csv
└── Smart_AI_Adaptive_Traffic_Dashboard_Final.pbix
```

## 9. How to Run the Python Files

### Step 1: Clone the repository

```bash
git clone https://github.com/VishwanathHarika17/Smart-AI-Adaptive-Traffic-Control.git
```

### Step 2: Open the project folder

```bash
cd Smart-AI-Adaptive-Traffic-Control
```

### Step 3: Install required libraries

```bash
pip install pandas numpy matplotlib
```

### Step 4: Run the Python scripts

```bash
python data_cleaning.py
python data_analysis.py
python data_visualization.py
```

Ensure the required dataset files are available in the project folder before running the scripts.

## 10. Project Outputs

The project produces:

- Cleaned traffic dataset.
- Traffic analysis reports.
- Area-wise traffic analysis.
- Traffic situation distribution.
- Monthly traffic volume trends.
- Python-generated visualization charts.
- Interactive Power BI dashboard.

## 11. Future Enhancements

- Integration of real-time traffic data.
- AI-based traffic prediction.
- Adaptive traffic signal timing recommendations.
- Integration with live traffic monitoring systems.
- Advanced congestion prediction and analysis.

## 12. Team Contributions

This project was developed collaboratively by a team of three members.

| Team Member | Responsibilities |
|---|---|
| Team Leader | Project Proposal and Data Analysis |
| Team Member 2 | Data Collection and Data Visualization |
| Team Member 3 | Data Cleaning and Interactive Dashboard |

 ## 13. Repository

GitHub: Smart AI Adaptive Traffic Control System

Project Domain: Artificial Intelligence and Data Analytics

Dataset: Bengaluru Traffic 2023–2024
