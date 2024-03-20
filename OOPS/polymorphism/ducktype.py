class Car:
    def __init__(self, fuel_type='gasoline', fuel_consumption_rate=25):
        self.fuel_type = fuel_type
        self.fuel_consumption_rate = fuel_consumption_rate

    def calculate_fuel_cost(self, distance):
        fuel_cost = (distance / self.fuel_consumption_rate) * self.get_fuel_price()
        return fuel_cost

    def get_fuel_price(self):
        # Simplified method to get fuel price based on fuel type
        if self.fuel_type == 'gasoline':
            return 3.0  # $3 per gallon for gasoline
        elif self.fuel_type == 'diesel':
            return 3.5  # $3.5 per gallon for diesel

class Bike:
    def __init__(self, fuel_type='gasoline', fuel_consumption_rate=50):
        self.fuel_type = fuel_type
        self.fuel_consumption_rate = fuel_consumption_rate

    def calculate_fuel_cost(self, distance):
        fuel_cost = (distance / self.fuel_consumption_rate) * self.get_fuel_price()
        return fuel_cost

    def get_fuel_price(self):
        # Simplified method to get fuel price based on fuel type
        if self.fuel_type == 'gasoline':
            return 3.0  # $3 per gallon for gasoline
        elif self.fuel_type == 'electric':
            return 0.1  # $0.1 per mile for electric bikes

class Truck:
    def __init__(self, fuel_type='diesel', fuel_consumption_rate=10):
        self.fuel_type = fuel_type
        self.fuel_consumption_rate = fuel_consumption_rate

    def calculate_fuel_cost(self, distance):
        fuel_cost = (distance / self.fuel_consumption_rate) * self.get_fuel_price()
        return fuel_cost

    def get_fuel_price(self):
        # Simplified method to get fuel price based on fuel type
        if self.fuel_type == 'gasoline':
            return 3.0  # $3 per gallon for gasoline
        elif self.fuel_type == 'diesel':
            return 3.5  # $3.5 per gallon for diesel

# Function to calculate total fuel cost for any vehicle
def calculate_total_fuel_cost(vehicle, distance):
    return vehicle.calculate_fuel_cost(distance)

# Create instances of different types of vehicles
car = Car()  # here fule_type and fuel_consumption_rate not passed so it will take default from constructor
bike = Bike()
truck = Truck()
#Duck Type does not care about the type of object just checks the
# behaviour/method is available for that object or not
# Calculate total fuel cost for each vehicle for a given distance
distance_traveled = 100  # miles
total_fuel_cost_car = calculate_total_fuel_cost(car, distance_traveled)
total_fuel_cost_bike = calculate_total_fuel_cost(bike, distance_traveled)
total_fuel_cost_truck = calculate_total_fuel_cost(truck, distance_traveled)

print("Total fuel cost for the car:", total_fuel_cost_car)
print("Total fuel cost for the bike:", total_fuel_cost_bike)
print("Total fuel cost for the truck:", total_fuel_cost_truck)
