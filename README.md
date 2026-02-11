# CityBike — Bike Sharing Analytics Platform

## Overview
CityBike is a backend analytics platform for a fictional bike-sharing service.
The project demonstrates object-oriented design, data analysis, algorithms,
numerical computing, visualization, and professional Git workflow.

## Dependencies
- Python 3.10+
- pandas
- numpy
- matplotlib

## Project Structure

```
citybike/
|── data/
│   ├── trips.csv        # Raw trip data
│   ├── stations.csv     # Station metadata
│   └── maintenance.csv  # Maintenance records
├── output/
│   ├── summary_report.txt
│   ├── top_stations.csv
│   ├── top_users.csv
│   └── figures/         # Exported PNG charts
|       |__trips_per_station.png
|
├── main.py              # Entry point — runs the full pipeline
├── models.py            # OOP domain classes (Entity, Bike, Station, …)
├── analyzer.py          # BikeShareSystem — data loading, cleaning, analytics
├── algorithms.py        # Custom sorting & searching + benchmarks
├── numerical.py         # NumPy computations (distances, stats, outliers)
├── visualization.py     # Matplotlib chart functions
├── pricing.py           # Strategy Pattern — pricing strategies
├── factories.py         # Factory Pattern — object creation from dicts
├── utils.py             # Validation & formatting helpers
├── generate_data.py     # Synthetic data generator (run once)
├── requirements.txt     # Python dependencies
|-- README.md            # Project description

```

## Setup

```bash
# 1. Clone the repository
git clone <repo-url>
cd city_bike

# 2. Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate    # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the pipeline
python main.py

```

## Features
- Object-oriented domain modeling

- Data loading, cleaning, and validation

- Custom sorting and searching algorithms

- Numerical analysis with NumPy

- Business analytics with Pandas

- Data visualization with Matplotlib

- Version control with Git


## Output
- Cleaned CSV datasets

- Summary report

- Analytics CSV exports

- PNG visualizations