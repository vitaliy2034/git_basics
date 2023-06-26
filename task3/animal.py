class Animal:
    def __repr__(self):
        return f'{self.__class__.__name__}()'


class Human(Animal):
    def __init__(self, tax_number):
        self.tax_number = tax_number

    def __repr__(self):
        return f'{self.__class__.__name__}(tax_number={self.tax_number!r})'


class Person(Human):
    def __init__(self, name, tax_number):
        super().__init__(tax_number)
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name!r}, tax_number={self.tax_number!r})'


class Enterprise:
    def __init__(self, pets=None):
        if pets is None:
            self.pets = []
        else:
            self.pets = pets

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self.pets.append(pet)

    def __repr__(self):
        return f'Enterprise(pets={self.pets})'


class Vaccine:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Vaccine(name={self.name})'


class Chip:
    def __init__(self, chip_id):
        self.chip_id = chip_id

    def __repr__(self):
        return f'Chip(chip_id={self.chip_id})'


class DogIDChip(Chip):
    pass


class CatIDChip(Chip):
    pass


class Pet(Animal):
    def __init__(self, owner, chip, vaccine=None):
        self.change_owner(owner)
        self.chip = chip
        self.vaccine = vaccine

    def change_owner(self, new_owner):
        self.owner = new_owner

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, Person):
            self.__owner = value
        else:
            err = f'{value!r} must be an instance'
            err += ' or subclass of Person.'
            raise ValueError(err)

    def __repr__(self):
        return f'{self.__class__.__name__}(owner={self.owner!r}, chip={self.chip!r}, vaccine={self.vaccine!r})'
