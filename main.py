from analyzer import BikeShareSystem
from visualization import (
    plot_tips_per_station,
    plot_monthly_trend,
    plot_duration_histogram,
    plot_duration_by_user_type,
)

def main() -> None:
    # Load and analyze data
    system = BikeShareSystem("data/bikeshare_data.csv")
    system.load_data()
    system.inspect_data()
    system.clean_trips()
    system.clean_stations()
    system.generate_summary()
    system.top_start_stations()
    system.top_users()  # Ensure data is clean before analysis
    
    # Generate visualizations
    df = system.trips_df  # Use cleaned trips data for visualizations
    plot_trips_per_station(df)
    plot_monthly_trend(df)
    plot_duration_histogram(df)
    plot_duration_by_user_type(df)


if __name__ == "__main__":
    main()