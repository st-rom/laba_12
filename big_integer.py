from node import TwoWayNode

class BigInteger:
    def __init__(self, initValue=0):
        #self.initValue = initValue
        self._head = TwoWayNode(str(initValue)[0])
        self._tail = self._head
        for i in str(initValue)[1:]:
            self._tail.next = TwoWayNode(i, self._tail)
            self._tail = self._tail.next

    def toString(self):
        string = ''
        probe = self._head
        while probe is not None:
            string += str(probe.data)
            probe = probe.next
        return string

    def __len__(self):
        length = 0
        if self._head is not None:
            probe = self._head
            while probe is not None:
                length += 1
                probe = probe.next
        return length

    def comparable(self, other):
        checker1 = self._head
        checker2 = other._head
        if len(self) > len(other):
            return str(self) + ' > ' + str(other)
        elif len(self) < len(other):
            return str(self) + ' < ' + str(other)
        else:
            while checker1.data != checker2.data or checker1 is not None:
                print(checker1.data)
                if int(checker1.data) > int(checker2.data):
                    return str(self) + ' > ' + str(other)
                elif int(checker1.data) < int(checker2.data):
                    return str(self) + ' < ' + str(other)
                elif checker1.data == checker2.data and checker1.next is None:
                    return str(self) + ' = ' + str(other)
                checker1 = checker1.next
                checker2 = checker2.next

    def arithmetic(self, rhsInt, oper):
        if oper == '+':
            ost = 0
            suma = ''
            while self._tail is not None or rhsInt._tail is not None:
                if self._tail is None:
                    helper = self._tail.data + ost
                elif rhsInt._tail is None:
                    helper = rhsInt._tail.data + ost
                else:
                    helper = int(self._tail.data) + int(rhsInt._tail.data) + ost
                ost = 0
                if helper >= 10:
                    ost = int(str(helper)[:-1])
                suma += str(abs(helper - (ost * 10)))
                self._tail = self._tail.previous
                rhsInt._tail = rhsInt._tail.previous
            return BigInteger(int(suma[::-1]))
        elif oper == '-':
            ost = 0
            suma = ''
            while self._tail is not None or rhsInt._tail is not None:
                if self._tail is None:
                    helper = self._tail.data + ost
                elif rhsInt._tail is None:
                    helper = rhsInt._tail.data + ost
                else:
                    helper = int(self._tail.data) + int(rhsInt._tail.data) + ost
                ost = 0
                if helper >= 10:
                    ost = int(str(helper)[:-1])
                suma += str(abs(helper - (ost * 10)))
                self._tail = self._tail.previous
                rhsInt._tail = rhsInt._tail.previous
            return BigInteger(int(suma[::-1]))

    def bitwise_ops(self, rhsInt, oper):
        fir = BigInteger(bin(int(self.toString()))[2:])
        sec = BigInteger(bin(int(rhsInt.toString()))[2:])
        number = ''
        ch1 = fir._tail
        ch2 = sec._tail
        if oper == '|':
            while fir._tail is not None or sec._tail is not None:
                if fir._tail is None:
                    data1 = 0
                    data2 = sec._tail.data
                    sec._tail = sec._tail.previous
                elif sec._tail is None:
                    data1 = fir._tail.data
                    data2 = 0
                    fir._tail = fir._tail.previous
                else:
                    data1 = fir._tail.data
                    data2 = sec._tail.data
                    fir._tail = fir._tail.previous
                    sec._tail = sec._tail.previous
                if int(data1) == 0 and int(data2) == 0:
                    number += '0'
                else:
                    number += '1'
            return BigInteger(int(number[::-1], 2))
        elif oper == '&':
            while fir._tail is not None or sec._tail is not None:
                if fir._tail is None:
                    data1 = 0
                    data2 = sec._tail.data
                    sec._tail = sec._tail.previous
                elif sec._tail is None:
                    data1 = fir._tail.data
                    data2 = 0
                    fir._tail = fir._tail.previous
                else:
                    data1 = fir._tail.data
                    data2 = sec._tail.data
                    fir._tail = fir._tail.previous
                    sec._tail = sec._tail.previous
                if int(data1) == 1 and int(data2) == 1:
                    number += '1'
                else:
                    number += '0'
            return BigInteger(int(number[::-1], 2))
        elif oper == '^':
            while fir._tail is not None or sec._tail is not None:
                if fir._tail is None:
                    data1 = 0
                    data2 = sec._tail.data
                    sec._tail = sec._tail.previous
                elif sec._tail is None:
                    data1 = fir._tail.data
                    data2 = 0
                    fir._tail = fir._tail.previous
                else:
                    data1 = fir._tail.data
                    data2 = sec._tail.data
                    fir._tail = fir._tail.previous
                    sec._tail = sec._tail.previous
                if (int(data1) == 0 and int(data2) == 0) or (int(data1) == 1 and int(data2) == 1):
                    number += '0'
                else:
                    number += '1'
            return BigInteger(int(number[::-1], 2))
        elif oper == '<<':
            for i in range(int(rhsInt.toString())):
                fir._tail.next = TwoWayNode(0, fir._tail)
                fir._tail = fir._tail.next
            return BigInteger(int(fir.toString(), 2))
        elif oper == '>>':
            left = len(fir) - int(rhsInt.toString())
            if left <= 0:
                return BigInteger(0)
            newbig = BigInteger(int(fir.toString()[0]))
            print(newbig, str(fir)[1:left], left)
            for i in str(fir)[1:left]:
                newbig._tail.next = TwoWayNode(int(i), newbig._tail)
                newbig._tail = newbig._tail.next
            return BigInteger(int(newbig.toString(), 2))
        else:
            print("This operation is not supported\nTry one of these: '|', '&', '^', '<<', '>>'")
            return 0

    def __str__(self):
        string = ''
        probe = self._head
        while probe is not None:
            string += str(probe.data)
            probe = probe.next
        return string

if __name__ == "__main__":
    a = BigInteger(22)
    print(a)
    b = BigInteger(52)
    print(a.comparable(b))
    print(str(a.bitwise_ops(b, '^')))
    print(a.arithmetic(b, '+'))
