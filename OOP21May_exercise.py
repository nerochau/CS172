# 🦸‍♂️ OOP Challenge: Superhero Management System

# 🎯 OBJECTIVE:
# Design a class that represents a superhero and allows you to:
# - Create superhero objects
# - Track and update their abilities
# - Use encapsulation to protect sensitive data
# - Control access to private details using getter/setter methods and decorators

# 🧠 Concepts Practiced:
# Classes, Objects, Attributes (public, protected, private),
# Methods, Self, __init__, Docstrings,
# Encapsulation, Getter/Setter, Property decorators,
# and Custom decorators to hide info.

# ----------------------------
# ✅ Step-by-step Instructions:
# ----------------------------
# Decorator to hide identity
def access_control(func):
    def wrapper(*args, **kwargs):
        print("Access denied: You cannot see the secret identity.")
        return func(*args, **kwargs)
    return wrapper

# 1. Define a class named Superhero.
class Superhero:
    """A superhero class that represent superheros and their superpowers"""

    def __init__(self, name, power, secret_identity="Unknown", abilities=None): #why put UnKnown
        self.name = name #public
        self._power = power #protected
        self.__secret_identity = secret_identity #private
        self.abilities = abilities or [] #empty

    def add_abilities(self, ability):
        #Add a method add_ability(self, ability) that appends to abilities.
        #self.add_abilities.append(ability)
        self.abilities.append(ability)
    
    def show_abilities(self):
        #Add a method show_abilities(self) that prints abilities joined by commas.
        print(f"{self.name}'s abilities: {', '.join(self.abilities)}")

# 7. Add getter and setter methods for secret_identity:
#    - get_secret_identity(self)
#    - set_secret_identity(self, new_identity)

    #Getter method for private attribute
    def get_secret_identity(self):
        return self.__secret_identity
    
    #setter methof for private attribute
    def set_secrete_identity(self, new_identity):
        if isinstance(new_identity, str):
            self.__secret_identity = new_identity
        else:
            print("Secrete identity must be a string!")
        
# 8. Use @property and @setter decorators for secret_identity to simplify getting and setting.
    @property
    def secret_identity(self):
        return self.__secret_identity
    
    @secret_identity.setter
    def secret_identity(self, value):
        if isinstance(value, str):
            self.__secret_identity = value
        else:
            print("Secret identity must be a string!")

    @access_control
    def hide_identity(self):
        return "Identity is hidden."

# 9. Add a method hide_identity(self) that returns "Identity is hidden".
# 10. Write a decorator function that, when applied to hide_identity, prints "Access denied: You cannot see the secret identity" before calling the method.

# 11. Create several superhero objects to test your implementation.

hero1 = Superhero("StormBreaker", "Electric Charge")
hero1.add_ability("Fly")
hero1.add_ability("Thunderbolt")
hero1.show_abilities()

print("\n--- Access secret identity using method ---")
print("Secret Identity:", hero1.get_secret_identity())

print("\n--- Access secret identity using @property ---")
print("Secret Identity:", hero1.secret_identity)

print("\n--- Change secret identity using setter method ---")
hero1.set_secret_identity("Zeus")
print("Updated Secret Identity:", hero1.get_secret_identity())

print("\n--- Change secret identity using @property.setter ---")
hero1.secret_identity = "Odin"
print("Updated Secret Identity:", hero1.secret_identity)

print("\n--- Try to hide identity ---")
print(hero1.hide_identity())


# After coding, run this script and test your superheroes!
# Let me know if you want me to review your code or give hints.
