class Car:
	# class variable
    speed_measurement = "KM/hr"

    def __init__(self, model, brand, color):
        # data members (instance variables)
        self.model = model
        self.brand = brand
        self.color = color

    # Behavior (instance methods)
    def info(self):
        print('Model:', self.model, 'Brand:', self.brand, 'Color:', self.color)

	# class method
    @classmethod
    def set_speed_measurement(cls, new_measurement):
        # modify class variable
        cls.speed_measurement = new_measurement
        return None

    @classmethod
    def get_speed_measurement(cls):
        # get class variable
        print(cls.speed_measurement)

    @staticmethod
    def get_region(name="West Africa"):
        return name



tesla = Car("Y", "Tesla", "Black")
tesla.info()

toyota = Car("Corolla", "Toyota", "Gold")
toyota.info()

# tesla.get_speed_measurement()
# toyota.get_speed_measurement()
# Car.get_speed_measurement()
# Car("Corolla", "Toyota", "Gold").get_speed_measurement()
# Car("Corolla", "Toyota", "Gold").speed_measurement

# print(tesla.get_region())
# print(toyota.get_region())
# print(Car.get_region())

# tesla.model = "X"
# toyota.model = "Camry"

# tesla.info()
# toyota.info()

# # Car.speed_measurement = "M/s"
# # Car.get_speed_measurement()

# tesla.speed_measurement = "D/t"
# tesla.get_speed_measurement()
# Car.get_speed_measurement()

# tesla.set_speed_measurement("M/r")
# tesla.get_speed_measurement()
# Car.get_speed_measurement()

# Car.speed_measurement = "M/s"
# Car.get_speed_measurement()
# print(tesla.model)

# del tesla.model

# del tesla.speed_measurement
# Car.get_speed_measurement()