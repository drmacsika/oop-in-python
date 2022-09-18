# Example 1

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


# Example 2
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