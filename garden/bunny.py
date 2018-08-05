import logging

logger = logging.getLogger(__name__)


class Bunny(object):
    """
    The Bunny is a state machine with three states, EATING, MOVING, and
    SLEEPING.
    """
    EATING = 1
    MOVING = 2
    SLEEPING = 3

    def __init__(self, garden):
        """
        Starts the bunny in the center of the garden.
        """
        self.pos = garden.center
        self.state = self.EATING
        self.stomach = 0

    def step(self):
        """
        Step through the state machine.
        """
        if self.state is self.EATING:
            # Eat all carrots into stomach, set count of cell to 0,
            # transition to MOVING.
            carrots = self.pos.carrots
            self.stomach += carrots
            self.pos.carrots = 0
            logger.info('Ate %s carrots from (%s, %s)', carrots, *self.pos.loc)
            self.state = self.MOVING
            return

        elif self.state is self.MOVING:
            # Look around at all adjacent cells, cull out-of-bounds and empty,
            # transition to SLEEPING if no adjacent cells, set current
            # position to adjacent cell with most carrots, transition to
            # EATING.
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
            # Nothing to do.
            logger.info('Sleeping.')
            return

        else:
            # Why would we be here? Cosmic-ray catch-all.
            logger.error("Invalid State")

    def run(self):
        """
        Run the state machine until SLEEPING.
        """
        while self.state is not self.SLEEPING:
            self.step()
