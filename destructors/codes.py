# Example of Creating a Destructor in Python When the Object is no Longer Referenced

# class Car:
# 	# constructor
#     # initialize instance variable
#     def __init__(self, model, brand, color):
#         # instance variables
#         self.model = model
#         self.brand = brand
#         self.color = color
#         print('Object is initialized')

#     def info(self):
#         print('Model:', self.model, 'Brand:', self.brand, 'Color:', self.color)

# 	# destructor
#     def __del__(self):
#         print('Destructor method is called for', self.model)
#         print('Object destroyed')
        
# # Instance of tesla accessing instance methods and variable
# tesla = Car("Y", "Tesla", "Black")
# tesla.info()

# toyota = Car("Camry", "Toyota", "Black")
# toyota.info()

# Output
# Object is initialized
# Model: Y Brand: Tesla Color: Black
# Object is initialized
# Model: Camry Brand: Toyota Color: Black
# Destructor method is called
# Object destroyed
# Destructor method is called
# Object destroyed


# ----------------------------------------------------------------
# Example of Creating a Destructor in Python When the Reference to the Object is Deleted

# class Car:
# 	# constructor
#     # initialize instance variable
#     def __init__(self, model, brand, color):
#         # instance variables
#         self.model = model
#         self.brand = brand
#         self.color = color
#         print('Object is initialized')

#     def info(self):
#         print('Model:', self.model, 'Brand:', self.brand, 'Color:', self.color)

# 	# destructor
#     def __del__(self):
#         print('Destructor method is called for', self.model)
#         print('Object destroyed')
        
# # Instance of tesla accessing instance methods and variable
# tesla = Car("Y", "Tesla", "Black")
# tesla.info()

# del tesla

# toyota = Car("Camry", "Toyota", "Black")
# toyota.info()

# Output
# Object is initialized
# Model: Y Brand: Tesla Color: Black
# Destructor method is called
# Object destroyed
# Object is initialized
# Model: Camry Brand: Toyota Color: Black
# Destructor method is called
# Object destroyed


# ----------------------------------------------------------------
# Example of a Destructor in Python When all references to the Object is not Deleted

# class Car:
# 	# constructor
#     # initialize instance variable
#     def __init__(self, model, brand, color):
#         # instance variables
#         self.model = model
#         self.brand = brand
#         self.color = color
#         print('Object is initialized')

#     def info(self):
#         print('Model:', self.model, 'Brand:', self.brand, 'Color:', self.color)

# 	# destructor
#     def __del__(self):
#         print('Destructor method is called for', self.model)
#         print('Object destroyed')
        
# # Instance of tesla accessing instance methods and variable
# tesla = Car("Y", "Tesla", "Black")
# tesla.info()
# tesla_ref = tesla
# del tesla
# # del tesla, tesla_ref
# toyota = Car("Camry", "Toyota", "Black")
# toyota.info()
# Output
# Object is initialized
# Model: Y Brand: Tesla Color: Black
# Destructor method is called
# Object destroyed


# ----------------------------------------------------------------
# Example of how Circular Referencing affects a Destructor
import time

class Vehicle():
    def __init__(self, id, car):
        self.id = id
        # saving reference of Car object
        self.dealer = car;
        print('Vehicle', self.id, 'created');

    def __del__(self):
        print('Vehicle', self.id, 'destroyed');


class Car():
    def __init__(self, id):
        self.id = id;
        # saving Vehicle class object in 'dealer' variable
        # Sending reference of Car object ('self') for Vehicle object
        self.dealer = Vehicle(id, self);
        print('Car', self.id, 'created')

    def __del__(self):
        print('Car', self.id, 'destroyed')


# create car object
c = Car(12)
# delete car object
del c
# ideally destructor must execute now

# to observe the behavior
time.sleep(8)