from LIF import LIF

class Synapse(object):

    def __init__(self, inputN: LIF, outputN: LIF, weight: int = 1):
        self.weight = weight
        self.inputN = inputN
        self.outputN = outputN
