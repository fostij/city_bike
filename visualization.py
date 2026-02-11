import matplotlib.pyplot as plt
import pandas as pd


# Bar charts - trips per start station
def plot_trips_per_station(df: pd.DataFrame) -> None:
    data = (
        df.groupby("start_station_id")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )
    plt.figure()
    data.plot(kind="bar")
    plt.title("Top 10 Start Stations by Trip Count")
    plt.xlabel("Start Station ID")
    plt.ylabel("Number of Trips")
    plt.tight_layout()
    plt.savefig("output/figures/trips_per_station.png")
    plt.close()

# Line charts - monthly trend
def plot_monthly_trend(df: pd.DataFrame) -> None:
    df["month"] = df["start_time"].dt.to_period("M")
    monthly = df.groupby("month").size()
    plt.figure()
    monthly.plot(kind="line")
    plt.title("Monthly Trip Volume Trend")
    plt.xlabel("Month")
    plt.ylabel("Trips")
    plt.tight_layout()
    plt.savefig("output/figures/monthly_trend.png")
    plt.close()

# Histograms - trip duration
def plot_duration_histogram(df: pd.DataFrame) -> None:
    plt.figure()
    plt.hist(df["duration_minutes"], bins=30)
    plt.title("Trip Duration Distribution")
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("output/figures/duration_histogram.png")
    plt.close()

# Box plot - duration by user type
def plot_duration_by_user_type(df: pd.DataFrame) -> None:
    plt.figure()
    df.boxplot(column="duration_minutes", by="user_type")
    plt.title("Trip Duration by User Type")
    plt.suptitle("")
    plt.xlabel("User Type")
    plt.ylabel("Duration (minutes)")
    plt.tight_layout()
    plt.savefig("output/figures/duration_by_user_type.png")
    plt.close()