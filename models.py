from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, id, created_add):
        self.id = id
        self.created_add = created_add

    @abstractmethod
    def __str__(self):
        return f"Entity(id={self.id}, created_add={self.created_add})"
    
    @abstractmethod
    def __repr__(self):
        return self.__str__()
    
    
class Bike(Entity):
        def __init__(self, id, created_add, model, status):
            super().__init__(id, created_add)
            self.id = id
            self.created_add = created_add
            self.model = model
            self.status = status

        def available(self):
             return self.status == "available"
        
        def in_use(self):
             return self.status == "in_use"
        
        def maintenance(self):
             return self.status == "maintenance"
        
class ClassicBike(Bike):
    def __init__(self, id, created_add, model, status):
        super().__init__(id, created_add, model, status)

class ElectricBike(Bike):
     def __init__(self, battery_level, max_range_km):
          super().__init__(id)
          self.battery_level = battery_level
          self.max.range_km = max_range_km


class Station(Entity):
     def __init__(self, station_id, name, capacity, latitude, longitude):
        super().__init__(id)
        self.station_id = station_id
        self.name = name
        self.capacity = capacity
        self.latitude = latitude
        self.longitude = longitude

class User(Entity):
     def __init__(self, user_id, name, email, user_type):
        super().__init__(id)
        if "@" not in email:
            raise ValueError("Invalid email address")
          
        self.user_id = user_id
        self.name = name
        self.email = email
        self.user_type = user_type


class CasualUser(User):
     def __init__(self, day_pass_count):
        super().__init__(id)
        self.day_pass_count = day_pass_count


class MemberUser(User):
     def __init__(self, membership_start, membership_end, tier):
        super().__init__(id)
        self.membership_start = membership_start
        self.membership_end = membership_end
        self.tier = tier


class Trip():
    def __init__(self, trip_id, user, bike, start_station, end_station, start_time, end_time, distance_km):
        self.trip_id = trip_id
        self.user = user
        self.bike = bike
        self.start_station = start_station
        self.end_station = end_station
        self.start_time = start_time
        self.end_time = end_time
        self.distance_km = distance_km

class MaintenanceRecord():
    def __init__(self, record_id, bike, date, maintenance_type, cost, description):
        self.record_id = record_id
        self.bike = bike
        self.date = date
        self.maintenance_type = maintenance_type
        self.cost = cost
        self.description = description

class BikeSharingSystem():
     def __init__(self, orchestrates_loading, cleaning, analysis, reporting):
        self.orchestrates_loading = orchestrates_loading
        self.cleaning = cleaning
        self.analysis = analysis
        self.reporting = reporting
          

    