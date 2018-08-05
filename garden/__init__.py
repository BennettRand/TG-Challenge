from .garden import Garden
from.bunny import Bunny


def eat(garden):
    garden = Garden.from_matrix(garden)
    bunny = Bunny(garden)

    bunny.run()

    return bunny.stomach
