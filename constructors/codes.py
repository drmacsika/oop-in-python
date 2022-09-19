# Creating a constructor
class Car:
	# constructor
    # initialize instance variable
    def __init__(self, model, brand, color):
        # instance variables
        self.model = model
        self.brand = brand
        self.color = color

    def info(self):
        print('Model:', self.model, 'Brand:', self.brand, 'Color:', self.color)
        
# Instance of tesla accessing instance methods and variable
tesla = Car("Y", "Tesla", "Black")
tesla.info()
# Output
# Model: Y Brand: Tesla Color: Black


# ----------------------------------------------------------------
# Example of default constructor
class Car:
    def info(self):
        print('Model:', "Y", 'Brand:', "Tesla", 'Color:', "Black")
        
# Instance of tesla accessing instance methods and variable
tesla = Car()
tesla.info()

# Output
# Model: Y Brand: Tesla Color: Black


# ----------------------------------------------------------------
# Example of Non-Parametrized Constructor
class Car:
    def __init__(self):
        self.model = "Y"
        self.brand = "Tesla"
        self.color = "Black"
	
    def info(self):
        print('Model:', self.model, 'Brand:', self.brand, 'Color:', self.color)
        
# Instance of tesla accessing instance methods and variable
tesla = Car()
tesla.info()
# Output
# Model: Y Brand: Tesla Color: Black


# ----------------------------------------------------------------
# Example of Parametrized Constructor
class Car:
    def __init__(self, model, brand, color):
        # instance variables
        self.model = model
        self.brand = brand
        self.color = color
	
    def info(self):
        print('Model:', self.model, 'Brand:', self.brand, 'Color:', self.color)
        
# Instance of tesla accessing instance methods and variable
tesla = Car("Y", "Tesla", "Black")
tesla.info()

# Output
# Model: Y Brand: Tesla Color: Black


# ----------------------------------------------------------------
# Example of Constructor Overloading
class Car:
    # constructor with one parameter
    def __init__(self, model):
        print("One argument constructor")
        self.model = model

    # constructor with two parameters
    def __init__(self, model, brand):
        print("constructor with two parameters")
        self.model = model
        self.brand = brand
	
	# constructor with three parameters
    def __init__(self, model, brand, color):
        print("constructor with three parameters")
        self.model = model
        self.brand = brand
        self.color = color

# creating first object
tesla1 = Car("Y", "Tesla", "Blackp")

# creating Second object
# tesla2 = Car("Y", "Tesla")


# ----------------------------------------------------------------
# Example of Chaining constructors
class Vehicle:
    # Constructor of Vehicle
    def __init__(self, category):
        print('Inside Vehicle Constructor')
        self.category = category

class Car(Vehicle):
    # Constructor of Car
    def __init__(self, category, brand):
        super().__init__(category)
        print('Inside Car Constructor')
        self.brand = brand

class ElectricCar(Car):
    # Constructor of Electric Car
    def __init__(self, category, model, brand):
        super().__init__(category, brand)
        print('Inside Electric Car Constructor')
        self.model = model

# Object of electric car
tesla = ElectricCar('Electric Car', "Y", "Tesla")
print(f'Category: {tesla.category}, Model: {tesla.model}, Brand={tesla.brand}')


# ----------------------------------------------------------------
# Example of Counting the number of objects in a class
class Car:
    counter = 0
    def __init__(self):
        Car.counter = Car.counter + 1

# creating objects
c1 = Car()
c2 = Car()
c2 = Car()
print("The number of Cars:", Car.counter)


# ----------------------------------------------------------------
# Example of return value in a class

# class ID:
#     def __init__(self, id):
#         self.id = id
#         return True

# d = ID(1)