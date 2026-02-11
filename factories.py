from datetime import datetime
from models import (
    Bike,
    ClassicBike,
    ElectricBike,
    User,
    CasualUser,
    MemberUser,
)

class BikeFactory:

    @staticmethod
    def create(data: dict) -> Bike:
        bike_type = data.get("bike_type")
        bike_id = data.get("bike_id")
        if bike_type == "classic":
            return ClassicBike(
                bike_id = bike_id,
                gear_count = 7
            )
        if bike_type == "electric":
            return ElectricBike(
                bike_id = bike_id,
                battery_level = 100,
                max_range_km = 50.0
            )
        raise ValueError(f"Unknown bike type: {bike_type}")


class UserFactory:

    @staticmethod
    def create(data: dict) -> User:
        user_type = data.get("user_type")
        user_id = data.get("user_id")
        name = data.get("name", "Unknown")
        email = data.get("email", "unknown@example.com")
        if user_type == "casual":
            return CasualUser(
                user_id = user_id,
                name = name,
                email = email
                day_pass_count = 0
            )
        if user_type == "member":
            start = datetime.now()
            end = start.replace(year=start.year + 1)
            return MemberUser(
                user_id = user_id,
                name = name,
                email = email
                membership_start = start,
                membership_end = end,
                tier = "basic"
            )
        raise ValueError(f"Unknown user type: {user_type}")