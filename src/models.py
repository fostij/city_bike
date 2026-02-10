"""
models.py

Domain models for the CityBike project.

This module contains ONLY object-oriented domain models.
No data loading, no pandas, no analytics.

All requirements from the project specification are strictly followed.
"""


from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional



class Entity(ABC):
    """
    Abstract base class for all domain entities.

    Required by the project:
    - id (read-only property)
    - created_at (read-only property)
    - abstract __str__ and __repr__ methods
    """

    def __init__(self, id: str, created_at: Optional[datetime] = None) -> None:
        if not id:
            raise ValueError("Entity ID must be a non-empty string.")
        self._id = id
        self._created_at = created_at or datetime.now()

    @property
    def id(self) -> str:
        """Return the unique identifier (read-only)."""
        return self._id

    @property
    def created_at(self) -> datetime:
        """Return the creation timestamp (read-only)."""
        return self._created_at  

    @abstractmethod
    def __str__(self) -> str:
        """Return a user-friendly string representation of the entity."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Return an unambiguous string representation of the entity for debugging."""
        pass
        


class Bike(Entity):
    """
    Represents a bike in the system.
    """

    VALID_STATUSES = {"available", "in_use", "maintenance"}

    def __init__(self, bike_id: str, bike_type: str, status: str):
        super().__init__(bike_id)
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid bike status: {status}")
        self.bike_type = bike_type
        self.status = status

    def __str__(self) -> str:
        return f"Bike {self.id} ({self.bike_type}, {self.status})"
    
    def __repr__(self):
        return (
            f"Bike(id={self.id!r}, "
            f"type={self.bike_type!r}, "
            f"status={self.status!r})"    
        )


class ClassicBike(Bike):
    def __init__(self, bike_id: str, gear_count: int):
        if gear_count <= 0:
            raise ValueError("Gear count must be a positive.")
        super().__init__(bike_id, "classic", "available")
        self.gear_count = gear_count

    def __str__(self) -> str:
        return f"ClassicBike {self.id} ({self.gear_count} gears)"
    
    def __repr__(self):
        return (
            f"ClassicBike(id={self.id!r}, "
            f"gears={self.gear_count!r})"
        )
    

class ElectricBike(Bike):
    def __init__(self, bike_id: str, battery_level: float, max_range_km: float):
        if not (0 <= battery_level <= 100):
            raise ValueError("Battery level must be between 0 and 100")
        if max_range_km <= 0:
            raise ValueError("Max range must be a positive")
        super().__init__(bike_id, "electric", "available")
        self.battery_level = battery_level
        self.max_range_km = max_range_km

    def __str__(self) -> str:
        return f"ElectricBike {self.id} ({self.battery_level} % battery)"
    
    def __repr__(self):
        return (
            f"ElectricBike(id={self.id!r}, " 
            f"battery_level={self.battery_level!r}, "
            f"max_range_km={self.max_range_km!r})"
        )

class Station(Entity):
    def __init__(self, station_id: str, name: str, capacity: int, latitude: float, longitude: float):
        super().__init__(station_id)
        if capacity <= 0:
            raise ValueError("Capacity must be a positive.")
        self.name = name
        self.capacity = capacity
        self.latitude = latitude
        self.longitude = longitude
        

    def __str__(self) -> str:
        return f"Station {self.name} (capacity {self.capacity})"
    
    def __repr__(self) -> str:
        return (
            f"Station(id={self.id!r}, "
            f"name={self.name!r}, "
            f"capacity={self.capacity!r})"
        )
    

class User(Entity):
    def __init__(self, user_id: str, name: str, email: str, user_type: str):
        super().__init__(user_id)
        if "@" not in email:
            raise ValueError("Invalid email address.")
        self.name = name
        self.email = email
        self.user_type = user_type

    def __str__(self) -> str:
        return f"User {self.name} ({self.user_type})"
    
    def __repr__(self) -> str:
        return (
            f"User(id={self.id!r}, "
            f"name={self.name!r}, "
            f"type={self.user_type!r})"
        )
    

class CasualUser(User):
    def __init__(self, user_id: str, name: str, email: str, day_pass_count: int):
        if day_pass_count < 0:
            raise ValueError("Day pass count cannot be negative")  
        super().__init__(user_id, name, email, "casual")
        self.day_pass_count = day_pass_count    


class MemberUser(User):
    def __init__(
            self,
            user_id: str,
            name: str,  
            email: str,
            membership_start: datetime,
            membership_end: datetime,
            tier: str
    ):
        if membership_end <= membership_start:
            raise ValueError("Membership end must be after start.")
        super().__init__(user_id, name, email, "member")
        self.membership_start = membership_start
        self.membership_end = membership_end
        self.tier = tier

class Trip:
    def __init__(
            self,
            trip_id: str,
            user: User,
            bike: Bike,
            start_station: Station,
            end_station: Station,
            start_time: datetime,
            end_time: datetime,
            distance_km: float,
    ):
        if end_time <= start_time:
            raise ValueError("End time must be after start time.")
        self.trip_id = trip_id
        self.user = user
        self.bike = bike
        self.start_station = start_station
        self.end_station = end_station
        self.start_time = start_time or datetime.now()
        self.end_time = end_time
        self.distance_km = distance_km

    @property
    def duration_minutes(self) -> float:
        return (self.end_time - self.start_time).total_seconds() / 60
    

class MaintenanceRecord:
    def __init__(
            self,
            record_id: str,
            bike: Bike,
            date: datetime,
            maintenance_type: str,
            cost: float,
            description: Optional[str] = None,
            
    ):
        if cost < 0:
            raise ValueError("Cost cannot be negative.")
        self.record_id = record_id
        self.bike = bike
        self.date = date
        self.maintenance_type = maintenance_type
        self.cost = cost
        self.description = description