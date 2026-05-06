# plant.py

import random

from organism import Organism


class Plant(Organism):

    def __init__(self, name, x, y):

        super().__init__(
            name=name,
            x=x,
            y=y,
            energy=20,
            health=50,
            symbol="P"
        )

    def move(self, world):

        return

    def reproduce(self, world):

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        random.shuffle(directions)

        for dx, dy in directions:

            new_x = self.x + dx
            new_y = self.y + dy

            if (
                world.is_valid(new_x, new_y)
                and world.get_organism(new_x, new_y) is None
            ):

                new_plant = Plant(
                    "Plant",
                    new_x,
                    new_y
                )

                world.add_organism(new_plant)

                break

    def act(self, world):

        self.gain_energy(1)

        self.age += 1

        if self.energy >= 35:

            self.lose_energy(10)

            self.reproduce(world)

        if self.age >= 30:

            self.die()