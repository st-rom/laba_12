from node import TwoWayNode

class BigInteger:
    def __init__(self, initValue="0"):
        self.initValue = initValue
        head = TwoWayNode(str(self.initValue)[0])
        tail = head
        for i in range(len(str(self.initValue)[1:])):
            tail.next = TwoWayNode(i, tail)
            tail = tail.next

    def toString(self):
        return str(self.initValue)

    def comparable(self, other):
        if self.initValue > other.initValue:
            return self.initValue + '>' + self.initValue
        elif self.initValue < other.initValue:
            return self.initValue + '<' + self.initValue
        else:
            return self.initValue + '=' + self.initValue

    def arithmetic(self, rhsInt):
        a = self.initValue + rhsInt.initValue
        b = self.initValue - rhsInt.initValue

    def bitwise_ops(self, rhsInt):
        pass
