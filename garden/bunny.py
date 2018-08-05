import logging

logger = logging.getLogger(__name__)


class Bunny(object):
    EATING = 1
    MOVING = 2
    SLEEPING = 3

    def __init__(self, garden):
        self.pos = garden.center
        self.state = self.EATING
        self.stomach = 0

    def step(self):
        if self.state is self.EATING:
            carrots = self.pos.carrots
            self.stomach += carrots
            self.pos.carrots = 0
            logger.info('Ate %s carrots from (%s, %s)', carrots, *self.pos.loc)
            self.state = self.MOVING
            return

        elif self.state is self.MOVING:
            return

        elif self.state is self.SLEEPING:
            return

        else:
            logger.error("Invalid State")