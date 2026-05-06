# animal.py

import random

from organism import Organism
from plant import Plant


class Animal(Organism):

    def __init__(self, name, x, y, energy, health, lifespan, speed, symbol):

        super().__init__(name, x, y, energy, health, symbol)

        self.lifespan = lifespan
        self.speed = speed

    def move(self, world):

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        dx, dy = random.choice(directions)

        new_x = self.x + dx
        new_y = self.y + dy

        if (
            world.is_valid(new_x, new_y)
            and world.get_organism(new_x, new_y) is None
        ):

            self.x = new_x
            self.y = new_y

    def check_death(self):

        if self.energy <= 0:
            self.die()

        if self.age >= self.lifespan:
            self.die()


class Herbivorous(Animal):

    def act(self, world):

        self.move(world)

        plant = world.get_adjacent_type(
            self.x,
            self.y,
            Plant
        )

        if plant:

            plant.die()

            self.gain_energy(10)

            print(f"{self.name} ate a plant")

        self.lose_energy(2)

        self.age += 1

        self.check_death()


class Rabbit(Herbivorous):

    def __init__(self, x, y):

        super().__init__(
            name="Rabbit",
            x=x,
            y=y,
            energy=random.randint(10, 20),
            health=100,
            lifespan=16,
            speed=5,
            symbol="R"
        )


class Cow(Herbivorous):

    def __init__(self, x, y):

        super().__init__(
            name="Cow",
            x=x,
            y=y,
            energy=random.randint(15, 30),
            health=120,
            lifespan=25,
            speed=2,
            symbol="C"
        )


class Deer(Herbivorous):

    def __init__(self, x, y):

        super().__init__(
            name="Deer",
            x=x,
            y=y,
            energy=random.randint(10, 25),
            health=100,
            lifespan=20,
            speed=4,
            symbol="D"
        )


class Carnivorous(Animal):

    def act(self, world):

        self.move(world)

        herbivore = world.get_adjacent_type(
            self.x,
            self.y,
            Herbivorous
        )

        if herbivore:

            herbivore.die()

            self.gain_energy(20)

            print(f"{self.name} hunted {herbivore.name}")

        self.lose_energy(3)

        self.age += 1

        self.check_death()


class Tiger(Carnivorous):

    def __init__(self, x, y):

        super().__init__(
            name="Tiger",
            x=x,
            y=y,
            energy=random.randint(20, 40),
            health=150,
            lifespan=30,
            speed=5,
            symbol="T"
        )


class Wolf(Carnivorous):

    def __init__(self, x, y):

        super().__init__(
            name="Wolf",
            x=x,
            y=y,
            energy=random.randint(15, 30),
            health=120,
            lifespan=22,
            speed=4,
            symbol="W"
        )