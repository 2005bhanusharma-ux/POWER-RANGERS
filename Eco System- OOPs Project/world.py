# world.py
import random
import time
from playsound import playsound
import os
from plant import Plant
from animal import Rabbit, Deer, Cow
from animal import Tiger, Wolf
from animal import Herbivorous, Carnivorous


class World:
    def __init__(self, width, height, plants, herbivores, carnivores):
        self.width = width
        self.height = height
        self.organisms = []
        self.turn = 0
        self.spawn_plants(plants)
        self.spawn_herbivores(herbivores)
        self.spawn_carnivores(carnivores)

    def add_organism(self, organism):
        self.organisms.append(organism)

    def is_valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get_organism(self, x, y):
        for organism in self.organisms:
            if organism.alive and organism.x == x and organism.y == y:
                return organism
        return None

    def get_adjacent_type(self, x, y, organism_type):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                organism = self.get_organism(nx, ny)
                if organism and isinstance(organism, organism_type):
                    return organism
        return None

    def spawn_plants(self, count):
        for _ in range(count):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if self.get_organism(x, y) is None:
                    self.add_organism(Plant("Plant", x, y))
                    break

    def spawn_herbivores(self, count):
        herbivore_classes = [Rabbit, Deer, Cow]
        for _ in range(count):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if self.get_organism(x, y) is None:
                    animal_class = random.choice(herbivore_classes)
                    self.add_organism(animal_class(x, y))
                    break

    def spawn_carnivores(self, count):
        carnivore_classes = [Tiger, Wolf]
        for _ in range(count):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if self.get_organism(x, y) is None:
                    animal_class = random.choice(carnivore_classes)
                    self.add_organism(animal_class(x, y))
                    break

    def clean_dead(self):
        self.organisms = [organism for organism in self.organisms if organism.alive]

    def stats(self):
        plants = sum(isinstance(o, Plant) for o in self.organisms)
        herbivores = sum(isinstance(o, Herbivorous) for o in self.organisms)
        carnivores = sum(isinstance(o, Carnivorous) for o in self.organisms)

        print(f"\nTurn : {self.turn}")
        print(f"Plants : {plants}")
        print(f"Herbivores : {herbivores}")
        print(f"Carnivores : {carnivores}")

        return plants, herbivores, carnivores

    def display(self):
        grid = [["." for _ in range(self.width)] for _ in range(self.height)]
        for organism in self.organisms:
            if organism.alive:
                grid[organism.y][organism.x] = organism.symbol
        for row in grid:
            print(" ".join(row))

    def update(self):
        random.shuffle(self.organisms)
        for organism in self.organisms[:]:
            if organism.alive:
                organism.act(self)
        self.clean_dead()
        self.turn += 1

    def game_over(self, message):
        print(f"\n{message}")
        print("Simulation Ended.")
        try:
            current_dir = os.path.dirname(__file__)
            sound_path = os.path.join(current_dir, "gameover.mp3")
            playsound(sound_path)
        except Exception:
            print("gameover.mp3 file not found")

    def run(self):
        while True:
            print("\n" * 2)
            self.display()
            plants, herbivores, carnivores = self.stats()
            self.update()
            time.sleep(0.5)

            if plants == 0:
                self.game_over("All plants are extinct.")
                break
            if herbivores == 0:
                self.game_over("All herbivores are extinct.")
                break
            if carnivores == 0:
                self.game_over("All carnivores are extinct.")
                break
