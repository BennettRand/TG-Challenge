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
            candidates = [self.pos.left, self.pos.right,
                          self.pos.up, self.pos.down]
            candidates = [c for c in candidates if
                          c is not None and c.carrots > 0]

            if len(candidates) <= 0:
                logger.info('No more carrots. Going to sleep.')
                self.state = self.SLEEPING

            else:
                self.pos = max(candidates, key=lambda x: x.carrots)
                logger.info('See %s carrots at (%s, %s), going there.',
                            self.pos.carrots, *self.pos.loc)
                self.state = self.EATING
            return

        elif self.state is self.SLEEPING:
            logger.info('Sleeping.')
            return

        else:
            logger.error("Invalid State")

    def run(self):
        while self.state is not self.SLEEPING:
            self.step()
