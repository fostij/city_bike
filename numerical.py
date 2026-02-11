import numpy as np

#Euclidean distance
def euclidean_distance(
    lat1: np.ndarray,
    lon1: np.ndarray,
    lat2: np.ndarray,
    lon2: np.ndarray,
) -> np.ndarray:
    """Calculate the Euclidean distance between two points given their latitude and longitude."""
    return np.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

#Trip Statistics
def trip_statistics(values: np.ndarray) -> dict:
    """Calculate basic statistics for a given array of values."""
    return {
        'mean': np.mean(values),
        'median': np.median(values),
        'std': np.std(values),
        'p95': np.percentile(values, 95),
    }

#Outlier Detection(Z-score)
def detect_outliers(values: np.ndarray, threshold: float = 3.0):
    """Detect outliers in an array of values using the Z-score method."""
    z_scores = (values - np.mean(values)) / np.std(values)
    return np.abs(z_scores) > threshold
