#adding attributes
class Superhero:
    def __init__(self, name, power, abilities=None):
        self.name = name
        self.power = power
        self.abilities = abilities or []

    def add_ability(self, ability):
        self.abilities.append(ability) #adding to the list
    
    def show_abilities(self):
        print(f"{self.name}'s abilities: {', '.join(self.abilities)}") #combining it to the attribute above

hero = Superhero("Jean Grey", "Telepathy")
hero.add_ability("Mind Control")
hero.add_ability("Telekinesis")
hero.show_abilities()

#-----------------------------------------getter and setter method----------------------------------------
class Superhero:
    """without the use of getter and setter"""
    def __init__(self, name):
        self.name = name

hero = Superhero("Flash")
hero.name = ""  # Oops! Empty name. Bad data 😬

class Superhero:
    """with getter and setter method"""
    def __init__(self, name):
        self.__name = name  # private attribute

    # ✅ Getter Method
    def get_name(self):
        return self.__name

    # ✅ Setter Method
    def set_name(self, new_name):
        if new_name:  # Don't allow empty names
            self.__name = new_name
        else:
            print("Invalid name!")

# Create object
hero = Superhero("Flash")

# Access name safely
print(hero.get_name())  # Flash

# Try to set a new name
hero.set_name("Barry Allen")
print(hero.get_name())  # Barry Allen

# Try to set an invalid name
hero.set_name("")       # Invalid name!


#-----------------------------------------property and setter method----------------------------------------
class Superhero:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):       # Acts like a getter
        return self.__name

    @name.setter
    def name(self, new_name):  # Acts like a setter
        if new_name:
            self.__name = new_name
        else:
            print("Invalid name!")

hero = Superhero("Flash")

print(hero.name)    # Access like attribute, not the method: hero.name()
hero.name = "Zoom"  # Set like attribute (but it's controlled)

#-----------------------------------------hide detail----------------------------------------
class Hero:
    def __init__(self, name, secret_identity):
        self.name = name
        self.__secret_identity = secret_identity  # private attribute

    def reveal_identity(self):
        print(f"{self.name}'s secret identity is {self.__secret_identity}")

"""WITHOUT THE REVEAL_IDENTITY
hero = Hero("Batman", "Bruce Wayne")
print(hero.__secret_identity)"""

hero = Hero("Batman", "Bruce Wayne")
hero.reveal_identity()  #no need to use print anymore

#with property
class Hero:
    def __init__(self, name, secret_identity, reveal=False):
        self.name = name
        self.__secret_identity = secret_identity
        self._reveal = reveal

    @property
    def secret_identity(self):
        if self._reveal:
            return self.__secret_identity
        return "Classified"

    def toggle_reveal(self):
        self._reveal = not self._reveal
    
hero = Hero("Batman", "Bruce Wayne")
print(hero.secret_identity)  # Classified
hero.toggle_reveal()
print(hero.secret_identity)  # Bruce Wayne