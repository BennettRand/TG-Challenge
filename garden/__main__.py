import logging

from . import eat

logger = logging.getLogger(__name__)


def main():
    garden1 = [[5, 7, 8, 6, 3],
               [0, 0, 7, 0, 4],
               [4, 6, 3, 4, 9],
               [3, 1, 0, 5, 8]]
    garden2 = [[1]]  # What happens with one cell?
    garden3 = [[0]]  # What happens in an empty garden?
    garden4 = [[1, 1, 1, 1],  # A garden with all equal cells?
               [1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1]]

    logger.info('Bunny ate %s carrots from garden1.', eat(garden1))
    logger.info('Bunny ate %s carrots from garden2.', eat(garden2))
    logger.info('Bunny ate %s carrots from garden3.', eat(garden3))
    logger.info('Bunny ate %s carrots from garden4.', eat(garden4))

    return


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    main()
