from abc import ABC, abstractmethod
from models import Trip

class PricingStrategy(ABC):

    @abstractmethod
    def calculate_price(self, trip: Trip) -> float:
        pass

class CasualPricing(PricingStrategy):
    PRICE_PER_MINUTE = 0.20

    def calculate_price(self, trip: Trip) -> float:
        return trip.duration_minutes * self.PRICE_PER_MINUTE

class MemberPricing(PricingStrategy):
    PRICE_PER_MINUTE = 0.10

    def calculate_price(self, trip: Trip) -> float:
        return trip.duration_minutes * self.PRICE_PER_MINUTE


class PeakHourPricing(PricingStrategy):
   BASE_PRICE = 0.15
   PEAK_MULTIPLIER = 1.5

   def calculate_price(self, trip: Trip) -> float:
    hour = trip.start_time.hour
    if 7 <= hour < 19 or 17 <= hour < 19:
        return trip.duration_minutes * self.BASE_PRICE * self.PEAK_MULTIPLIER
    return trip.duration_minutes * self.BASE_PRICE