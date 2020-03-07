from LIF import LIF
from typing import List

class Synapse(object):

    def __init__(self, inputN: LIF, outputN: LIF, weight: float = 1):
        self.weight = weight
        self.inputN = inputN
        self.outputN = outputN

    def weightedOutput(self, simulatedTime:float):
        return self.weight * self.inputN.potentialAt(simulatedTime)

    @staticmethod
    def calculateSynapsesOutput(simulatedTime:float, synapses:List[Synapse]):
        sum(s.weightedOutput(simulatedTime) for s in synapses)