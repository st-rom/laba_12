# Implementation of the Polynomial ADT using a sorted linked list.


class Polynomial:
    # Create a new polynomial object.
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead

    # Return the degree of the polynomial.
    def degree(self):
        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.degree

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        curNode = self._polyHead
        while curNode is not None:
            if curNode.degree == degree:
                return curNode.coefficient
            curNode = curNode.next
        return 0.0

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        curNode = self._polyHead
        while curNode is not None:
            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next
        return result

    # Polynomial addition: newPoly = self + rhsPoly.
    #def __add__(self, rhsPoly):
    #    pass

    # Polynomial subtraction: newPoly = self - rhsPoly.
    def __sub__(self, rhsPoly):
        newPoly = self - rhsPoly
        return newPoly

    # Polynomial multiplication: newPoly = self * rhsPoly.
    def __mul__(self, rhsPoly):
        newPoly = self * rhsPoly
        return newPoly

    def simple_add(self, rhsPoly):
        newPoly = Polynomial()
        if self.degree() > rhsPoly.degree():
            maxDegree = self.degree()
        else:
            maxDegree = rhsPoly.degree()

        i = maxDegree
        while i >= 0:
            value = self[i] + rhsPoly[i]
            newPoly._appendTerm(i, value)
            i -= 1
        return newPoly

    # Helper method for appending terms to the polynomial.
    def _appendTerm(self, degree, coefficient):
        if coefficient != 0.0:
            newTerm = _PolyTermNode(degree, coefficient)
            if self._polyHead is None:
                self._polyHead = newTerm
            else:
                self._polyHead.next = newTerm
            self._polyTail = newTerm

    def __add__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, "Addition only allowed on non -empty polynomials."
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        # Add corresponding terms until one list is empty.
        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree
                value = nodeA.coefficient + nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm(degree, value)

        # If self list contains more terms append them.
        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        # Or if rhs contains more terms append them.
        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newPoly

    def __str__(self):
        jack = ''
        pol = self._polyHead
        for i in range(self.degree()):
            jack += pol
            pol = pol.next
        return jack
        pass

# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None


if __name__ == "__main__":
    a = Polynomial(2, 4)
    b = Polynomial(1, 3)
    print(a.degree())
    a._appendTerm(0, 4)
    a = a.simple_add(b)
    print(a.evaluate(1))
