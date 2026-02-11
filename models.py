"""
models.py

Domain-Modelle für das City Bike Sharing System.

Dieses Modul enthält alle Kern-Entitäten des Systems, basierend auf OOP-Prinzipien:

- Entity: Abstrakte Basisklasse
- Bike, Station, User: Konkrete Domänenobjekte
- Trip, MaintenanceRecord: Zusätzliche Geschäftsobjekte

Prinzipien:
- Abstraktion
- Vererbung
- Kapselung (@property)
- Einheitliche String-Darstellung (__str__, __repr__)
"""


from abc import ABC, abstractmethod
from datetime import datetime



class Entity(ABC):
    """
    Abstrakte Basisklasse für alle Entitäten.

    Jede Entität besitzt:
    - eine eindeutige ID
    - ein Erstellungsdatum

    Unterklassen müssen __str__ und __repr__ implementieren.
    """  

    def __init__(self, id: str, created_at: datetime) -> None:
        """
        Initialisiert eine neue Entität.

        :param entity_id: Eindeutige ID
        """
        if not id:
            raise ValueError("Entity ID must be a non-empty string.")
        self._id = id # private ID zur Sicherstellung der Kapselung
        self._created_at = datetime() # Zeitpunkt der Erstellung

    @property
    def id(self) -> str:
        """Gibt die eindeutige ID zurück."""
        return self._id

    @property
    def created_at(self) -> datetime:
        """Gibt das Erstellungsdatum zurück."""
        return self._created_at  

    @abstractmethod
    def __str__(self) -> str:
        """Muss von jeder Unterklasse implementiert werden."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Muss von jeder Unterklasse implementiert werden."""
        pass
        


class Bike(Entity):
    """
    Repräsentiert ein Fahrrad im System.
    """

    VALID_STATUSES = {"available", "in_use", "maintenance"}

    def __init__(self, bike_id: str, bike_type: str, status: str):
        """
        Initialisiert ein neues Bike.

        :param bike_id: Eindeutige ID
        :param bike_type: Typ des Fahrrads (z.B. Standard)
        :param status: Status (z.B. 'available', 'in_use')
        """
        super().__init__(bike_id)
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid bike status: {status}")
        self.bike_type = bike_type
        self.status = status

    def __str__(self) -> str:
        """Benutzerfreundliche Darstellung des Bikes."""
        return f"Bike {self.id} ({self.bike_type}, {self.status})"
    
    def __repr__(self):
        """Technische Darstellung des Bikes."""
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
        """
        Benutzerfreundliche Darstellung des Fahrrads.
        """
        return f"ClassicBike {self.id} ({self.gear_count} gears)"
    
    def __repr__(self):
        """
        Technische Repräsentation des Fahrrads.
        """
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
    """
    Repräsentiert eine Bike-Station.
    """
    def __init__(self, station_id: str, name: str, capacity: int, latitude: float, longitude: float):
        """
        Initialisiert eine neue Station.

        :param station_id: Eindeutige ID
        :param name: Name der Station
        :param capacity: Maximale Kapazität
        """
        super().__init__(station_id)
        if capacity <= 0:
            raise ValueError("Capacity must be a positive.")
        self.name = name
        self.capacity = capacity
        self.latitude = latitude
        self.longitude = longitude
        

    def __str__(self) -> str:
        """Benutzerfreundliche Darstellung der Station."""
        return f"Station {self.name} (capacity {self.capacity})"
    
    def __repr__(self) -> str:
        """Technische Darstellung der Station."""
        return (
            f"Station(id={self.id!r}, "
            f"name={self.name!r}, "
            f"capacity={self.capacity!r})"
        )
    

class User(Entity):
    """
    Repräsentiert einen Benutzer des Systems.
    """
    def __init__(self, user_id: str, name: str, email: str, user_type: str):
        """
        Initialisiert einen Benutzer.

        :param user_id: Eindeutige ID
        :param user_type: Typ des Benutzers (z.B. 'customer', 'admin')
        """
        super().__init__(user_id)
        if "@" not in email:
            raise ValueError("Invalid email address.")
        self.name = name
        self.email = email
        self.user_type = user_type

    def __str__(self) -> str:
        """Benutzerfreundliche Darstellung des Benutzers."""
        return f"User {self.name} ({self.user_type})"
    
    def __repr__(self) -> str:
        """Technische Darstellung des Benutzers."""
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
    """
    Repräsentiert eine einzelne Fahrt.
    """
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
        """
        Initialisiert eine Fahrt.

        :param trip_id: Eindeutige ID
        :param bike_id: ID des Fahrrads
        :param user_id: ID des Benutzers
        :param start_station_id: Startstation
        :param end_station_id: Endstation
        :param start_time: Startzeit
        :param end_time: Endzeit
        :param distance_km: Fahrdistanz
        """
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
        """Berechnet die Fahrtdauer in Minuten."""
        return (self.end_time - self.start_time).total_seconds() / 60
    
    def __str__(self) -> str:
        """Benutzerfreundliche Darstellung der Fahrt."""
        return f"Trip {self.trip_id} ({self.duration_minutes:.1f} min)"

    def __repr__(self) -> str:
        """Technische Darstellung der Fahrt."""
        return (
            f"Trip(id='{self.trip_id}', "
            f"bike='{self.bike_id}', "
            f"user='{self.user_id}', "
            f"duration={self.duration_minutes:.1f})"
        )
    

class MaintenanceRecord:
    """
    Repräsentiert einen Wartungseintrag für ein Fahrrad.
    """
    def __init__(
            self,
            record_id: str,
            bike: Bike,
            date: datetime,
            maintenance_type: str,
            cost: float,
            description: str,
            
    ):
        """
        Initialisiert einen Wartungseintrag.

        :param record_id: Eindeutige ID
        :param bike_id: ID des Fahrrads
        :param date: Datum der Wartung
        :param cost: Kosten
        """
        if cost < 0:
            raise ValueError("Cost cannot be negative.")
        self.record_id = record_id
        self.bike = bike
        self.date = date
        self.maintenance_type = maintenance_type
        self.cost = cost
        self.description = description

    def __str__(self) -> str:
        """Benutzerfreundliche Darstellung des Wartungseintrags."""
        return f"Maintenance {self.record_id} (bike={self.bike_id})"

    def __repr__(self) -> str:
        """Technische Darstellung des Wartungseintrags."""
        return (
            f"MaintenanceRecord(id='{self.record_id}', "
            f"bike='{self.bike_id}', "
            f"cost={self.cost}, "
            f"date='{self.date}')"
        )