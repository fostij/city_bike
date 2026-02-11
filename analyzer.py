import pandas as pd

class BikeShareSystem():
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.trips_df = None
        self.stations_df = None
        self.maintenance_df = None

    def load_data(self) -> None:
        self.trips_df = pd.read_csv('data/trips.csv', parse_dates=['start_time', 'end_time'])
        self.stations_df = pd.read_csv('data/stations.csv')
        self.maintenance_df = pd.read_csv('data/maintenance.csv')

    def inspect_data(self) -> None:
        print(self.trips_df.info())
        print(self.trips_df.isnull().sum())
       
    def clean_trips(self) -> None:
        self.trips_df = self.trips_df[self.trips_df["end_time"] > self.trips_df["start_time"]]
        self.trips_df["duration_minutes"].fillna(self.trips_df["duration_minutes"].median(), inplace=True)
        self.trips_df["distance_km"].fillna(self.trips_df["distance_km"].median(), inplace=True)
        self.trips_df["status"].fillna("completed", inplace=True)
        self.trips_df.drop_duplicates(inplace=True)
        self.trips_df.to_csv("data/trips_clean.csv", index=False)

    def clean_stations(self) -> None:
        self.stations_df.drop_duplicates(inplace=True)
        self.stations_df = self.stations_df[self.stations_df["capacity"] > 0]
        self.stations_df.to_csv("data/stations_clean.csv", index=False)

    def total_trips(self) -> int:
        return len(self.trips_df)

    def total_distance(self) -> float:
        return self.trips_df["distance_km"].sum()

    def average_duration(self) -> float:
        return self.trips_df["duration_minutes"].mean()

    def top_start_stations(self) -> pd.DataFrame:
        result = (
            self.trips_df
            .groupby("start_station_id")
            .size()
            .sort_values(ascending=False)
            .head(10)
            .reset_index(name="trip_count")
        )
        result.to_csv("data/top_stations.csv", index=False)
        return result

    def peak_hours(self) -> pd.Series:
        hours = self.trips_df["start_time"].dt.hour
        return hours.value_counts().sort_index()

    def trips_by_weekday(self) -> pd.Series:
        weekdays = self.trips_df["start_time"].dt.day_name()
        return weekdays.value_counts()

    def avg_distance_by_user_type(self) -> pd.Series:
        return self.trips_df.groupby("user_type")["distance_km"].mean()

    def top_users(self) -> pd.DataFrame:
        result = (
            self.trips_df
            .groupby("user_id")
            .size()
            .sort_values(ascending=False)
            .head(15)
            .reset_index(name="trip_count")
        )
        result.to_csv("output/top_users.csv", index=False)
        return result

    def maintenance_cost_by_bike_type(self) -> pd.Series:
        return self.maintenance_df.groupby("bike_type")["cost"].sum()

    def generate_summary(self) -> None:
        with open("output/summary_report.txt", "w") as f:
            f.write(f"Total Trips: {self.total_trips()}\n")
            f.write(f"Total Distance: {self.total_distance():.2f} km\n")
            f.write(f"Average Duration: {self.average_duration():.2f} minutes\n")
        