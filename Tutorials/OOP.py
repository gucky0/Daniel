# class: blueprint for creating class objects ( nothing created yet )
class Car:
    def __init__(self):
        pass

# 2 different instance ( multiple specific cases )
nissan = Car()
toyota = Car()

# print(Ferrari == Toyota) 
# False


class Car:
    functionalCostPerMth = 700 
    def __init__(self, price, topspeed):
        self.price = price
        self.topspeed = topspeed

audi    = Car(price = 36_430, topspeed = 203)
ferrari = Car(price = 232_525, topspeed = 320)

# print(audi.functionalCostPerMth)
# 700

# print(ferrari.price)
# 232525


# Docstring: show useful information when we print class instance (object)
class Car:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} bought this car!"

# honda = Car(name = "Tony")
# print(honda)


class Car:
    servicingFeePerMth = 300
    def __init__(self, mthsUsed):
        self.mthsUsed = mthsUsed

    # Another instance method
    def payment(self):
        return f"you would need to pay {self.mthsUsed * self.servicingFeePerMth} in {self.mthsUsed} months."

# porsche = Car(24)
# print(porsche.payment())

# Application: UNICLO logistics

class Clothing(object):
    def __init__(self, type, color, size, price=None):
        self.type = type
        self.color = color
        self.size = size
        self.price = price

    def set_price(self, price):
        """Set the price of an item of clothing."""
        self.price = price
        print(f"Setting the price of the {self.color} {self.type} to ${price}.")

    def get_price(self):
        """Get the price of an item of clothing, if price is set."""
        try:
            print(f"The {self.color} {self.type} costs ${self.price}.")
        except:
            print(f"The price of the {self.color} {self.type} hasn't been set yet!")

    def promote(self, percentage):
        """Lower the price, if initial price is set."""
        try:
            self.price = self.price * (1-percentage/100)
            print(f"The price of the {self.color} {self.type} has been reduced by {percentage} percent! It now only costs ${self.price:.0f}.")
        except:
            print(f"Oops. Set an initial price first!")

bluejeans = Clothing("jeans", "blue", 12)
redtshirt = Clothing("t-shirt", "red", 10, 10)

# print("------------------- blue jeans -------------------")
# bluejeans.promote(20)
# bluejeans.set_price(30)
# bluejeans.get_price()

# print()
# print("------------------- red t-shirt -------------------")
# redtshirt.get_price()
# redtshirt.promote(20)

# print()
# print("Great Singapore Sale - 16% OFF for ALL items")
# for shirt in (redtshirt, bluejeans):
#     shirt.promote(16)

# child classes: extend (inherit parent atributes) or override current atributes

# Defining parent class
# class Parent():
      
#     # Constructor
#     def __init__(self):
#         self.value = "Inside Parent"
          
#     # Parent's show method
#     def show(self):
#         print(self.value)
          
# # Defining child class
# class Child(Parent):
      
#     # Constructor
#     def __init__(self):
#         Parent.__init__(self)
#         # self.value = "Child"
          
#     # Child's show method
#     def show(self):
#         print(self.value)
# # Driver's code
# obj1 = Parent()
# obj2 = Child()
  
# obj1.show()
# obj2.show()




class FastFoodOrder():
    def __init__(self, name,  price = 0, *items):
        self.name = name
        self.price = price

        self.items = []
        for item in items:
            self.items.append(item)
    def __str__(self):
        return f"name: {self.name}, items: {self.items}, price: {self.price}\n"
        

alex = FastFoodOrder("alex", 2.0, "sprite","coke")
# alex.items.remove("coke")
print(alex)       


class FastFoodItems(FastFoodOrder):
    def __init__(self, name,  price = 0, *items):
        FastFoodOrder.__init__(self, name, price, *items)
        # self.pay()

    def pay(self):
        dict_items = {  "fries": 1.70,
                        "coke" : 1.30,
                        "McChx": 2.00   }
        for item in self.items[:]:
            if dict_items.get(item):
                self.price += dict_items[item]
            else:
                print(f"{item} does not exist.")
                self.items.remove(item)

alex = FastFoodItems("alex",0, "sprite","coke")
print(alex)
alex.pay()
print(alex)

# alex = FastFoodItems("alex")
# alex.buy("fries")






# class Combo(FastFoodOrder):
#     def discountedPrice(self):
#         # self.name = name
#         self.price = self.price*0.9


# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
####
##miles = Dog("Miles", 4, "Jack Russell Terrier")
##buddy = Dog("Buddy", 9, "Dachshund")
##jack = Dog("Jack", 3, "Bulldog")
##jim = Dog("Jim", 5, "Bulldog")
####


# class JackRussellTerrier(Dog):
#     def speak(self, sound="Arf"):
#         return f"{self.name} said {sound}"
####
####miles.speak("Grrr")
####jim = Bulldog("Jim", 5)
####jim.speak("Woof")
####miles = JackRussellTerrier("Miles", 4)
####miles.speak()
####
# class JackRussellTerrier(Dog):
#     def speak(self, sound="Arf"):
#         return super().speak(sound) #uses parent method
# ####
####miles.speak()
####
####'''
##use type to find out child class inheritance: type(objName)
##use isinstance to find out any class inheritance: isinstance(objName, className)
####'''
####
####'''








class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"











     
####
####class GoldenRetriever(Dog):
####    def speak(self, sound="Bark"):
####        return super().speak(sound)
####'''
##
##a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
##
####for key in a_dict.keys():
####     print(key)
####
####for value in a_dict.values():
####     print(value)
####
####for key, value in a_dict.items():
####     print(key, '->', value)
##
##prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
##
##for k, v in prices.items():
##    v = v * 0.9
##    prices[k] = round(v, 2)  
##
##prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
##for key in list(prices.keys()):  
##     if key == 'orange':
##         del prices[key]
##
##incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
##non_citric = {k: incomes[k] for k in incomes.keys() - {'orange'}}
##
##a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
##new_dict = {}
##for key, value in a_dict.items():
##    new_dict[value] = key
##
##a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
##new_dict = {value: key for key, value in a_dict.items()}
##
##a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
##new_dict = {}  # Create a new empty dictionary
##for key, value in a_dict.items():
##    # If value satisfies the condition, then store it in new_dict
##    if value <= 2:
##        new_dict[key] = value
##
##a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
##new_dict = {k: v for k, v in a_dict.items() if v <= 2}
##
##incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
##total_income = 0.00
##for value in incomes.values():
##    total_income += value  # Accumulate the values in total_income
##
##incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
##total_income = sum([value for value in incomes.values()])
##
##total_income = sum(incomes.values())
##
##objects = ['blue', 'apple', 'dog']
##categories = ['color', 'fruit', 'pet']
##a_dict = {key: value for key, value in zip(categories, objects)}
##
##incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
##for key in sorted(incomes):
##    #print(key, '->', incomes[key])
##
##incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
##sorted_income = {k: incomes[k] for k in sorted(incomes)} #sort by name
##
##incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
##for key in sorted(incomes, reverse=True):
##    #print(key, '->', incomes[key])
##     
