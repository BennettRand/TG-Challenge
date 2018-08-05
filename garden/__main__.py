import logging

from .garden import Garden


def eat(garden):
    garden = Garden.from_matrix(garden)

    logging.debug(garden.cells[0][0].loc)
    logging.debug(garden.cells[0][0].left)
    logging.debug(garden.cells[0][0].right.loc)
    logging.debug(garden.cells[0][0].up)
    logging.debug(garden.cells[0][0].down.loc)


def main():
    garden1 = [[5, 7, 8, 6, 3],
               [0, 0, 7, 0, 4],
               [4, 6, 3, 4, 9],
               [3, 1, 0, 5, 8]]

    eat(garden1)

    return


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    main()
