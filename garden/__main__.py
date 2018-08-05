import logging

from .garden import Garden
from.bunny import Bunny

logger = logging.getLogger(__name__)


def eat(garden):
    garden = Garden.from_matrix(garden)
    bunny = Bunny(garden)

    bunny.run()

    return bunny.stomach


def main():
    garden1 = [[5, 7, 8, 6, 3],
               [0, 0, 7, 0, 4],
               [4, 6, 3, 4, 9],
               [3, 1, 0, 5, 8]]

    logger.info('Bunny ate %s carrots from garden1.', eat(garden1))

    return


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    main()
