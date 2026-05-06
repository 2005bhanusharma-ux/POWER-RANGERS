# organism.py

from abc import ABC, abstractmethod


class Organism(ABC):

    def __init__(self, name, x, y, energy, health, symbol):

        self.name = name

        self.x = x
        self.y = y

        self.energy = energy

        self.health = health

        self.symbol = symbol

        self.alive = True

        self.age = 0

    @property
    def energy(self):

        return self.__energy

    @energy.setter
    def energy(self, value):

        self.__energy = value

    def gain_energy(self, amount):

        self.__energy += amount

    def lose_energy(self, amount):

        self.__energy -= amount

        if self.__energy < 0:
            self.__energy = 0

    def die(self):

        self.alive = False

    def eat(self, food):

        self.gain_energy(food.energy)

    @abstractmethod
    def move(self, world):
        pass

    @abstractmethod
    def act(self, world):
        pass