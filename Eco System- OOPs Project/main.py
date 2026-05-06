# main.py

from world import World


def main():

    world = World(
        width=20,
        height=20,
        plants=50,
        herbivores=15,
        carnivores=5
    )

    world.run()


if __name__ == "__main__":

    main()