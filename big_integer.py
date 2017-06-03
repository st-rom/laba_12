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
            #print(str(self) + ' > ' + str(other))
            return '>'
        elif len(self) < len(other):
            #print(str(self) + ' < ' + str(other))
            return '<'
        else:
            while checker1.data != checker2.data or checker1 is not None:
                if int(checker1.data) > int(checker2.data):
                    #print(str(self) + ' > ' + str(other))
                    return '>'
                elif int(checker1.data) < int(checker2.data):
                    #print(str(self) + ' < ' + str(other))
                    return '<'
                elif checker1.data == checker2.data and checker1.next is None:
                    #print(str(self) + ' = ' + str(other))
                    return '='
                checker1 = checker1.next
                checker2 = checker2.next

    def arithmetic(self, rhsInt, oper):
        if oper == '+':
            ost = 0
            suma = ''
            while self._tail.previous is not None or rhsInt._tail.previous is not None:
                if self._tail.previous is None and suma != '':
                    rhsInt._tail = rhsInt._tail.previous
                    helper = int(rhsInt._tail.data) + ost
                elif rhsInt._tail.previous is None and suma != '':
                    self._tail = self._tail.previous
                    helper = int(self._tail.data) + ost
                else:
                    if suma != '':
                        self._tail = self._tail.previous
                        rhsInt._tail = rhsInt._tail.previous
                    helper = int(self._tail.data) + int(rhsInt._tail.data) + ost
                ost = 0
                if helper >= 10 and self._tail.previous is None and rhsInt._tail.previous is None:
                    ost = int(str(helper)[:-1])
                    suma += str(abs(helper - (ost * 10)))
                    suma += str(abs(ost * 10))
                elif helper >= 10:
                    ost = int(str(helper)[:-1])
                    suma += str(abs(helper - (ost * 10)))
                else:
                    suma += str(abs(helper - (ost * 10)))
                #print(suma, helper, ost, self._tail.data, rhsInt._tail.data)
            return BigInteger(int(suma[::-1]))
        elif oper == '-':
            totake = 0
            ost = 0
            vid = False
            one = self
            two = rhsInt
            if self.comparable(rhsInt) == '<':
                vid = True
                two = self
                one = rhsInt
            suma = ''
            while one._tail is not None or two._tail is not None:
                if two._tail is None:
                    helper = int(one._tail.data) + ost
                else:
                    if int(one._tail.data) - int(two._tail.data) - totake < 0 and one._tail.previous is not None:
                        ost += 10
                    helper = int(one._tail.data) - int(two._tail.data) + ost - totake
                    #print('uu', helper, int(one._tail.data), int(two._tail.data), ost, totake)
                if helper < 0:
                    if vid is True:
                        vid = False
                    elif vid is False:
                        vid = True
                totake = int(ost / 10)
                ost = 0
                suma += str(abs(helper))
                one._tail = one._tail.previous
                if two._tail is not None:
                    two._tail = two._tail.previous
            if vid is True:
                return BigInteger(int('-' + suma[::-1]))
            else:
                return BigInteger(int(suma[::-1]))
        elif oper == '*':
            ost = 0
            suma = ''
            dob = []
            abu = self._tail
            self.t = self._tail
            print(self, rhsInt)
            for i in range(len(rhsInt)):
                for j in range(len(self)):
                    if self.t is None and rhsInt._tail is None:
                        break
                    if self.t is None:
                        helper = int(rhsInt._tail.data) + ost
                    elif rhsInt._tail is None:
                        helper = int(self.t.data) + ost
                    else:
                        helper = (int(self.t.data) * int(rhsInt._tail.data)) + ost
                    print('tt', helper, abu.data, ost)
                    if helper >= 10 and self.t.previous is None:
                        #print('1')
                        ost = int(helper / 10)
                        suma += str(abs(helper - (ost * 10)))
                        suma += str(abs(ost * 10))
                    elif helper >= 10 and self.t.previous is not None:
                        #print('2')
                        ost = int(helper/10)
                        suma += str(abs(helper - (ost * 10)))
                    else:
                        #print('3')
                        ost = int(helper / 10)
                        suma += str(abs(helper))
                    print('ss', suma)
                    self.t = self.t.previous
                dob.append(suma[::-1] + ('0' * i))
                suma = ''
                ost = 0
                if rhsInt._tail is not None:
                    rhsInt._tail = rhsInt._tail.previous
                self.t = abu
            #print('d', dob)
            numb = BigInteger(int(dob[0]))
            for i in dob[1:]:
                ar = BigInteger(int(i))
                #print('a', ar, numb)
                numb = numb.arithmetic(ar, '+')
                #print('b', ar, numb)
            return numb
        elif oper == '**':
            numb = self
            bro = BigInteger(int(self.toString()))
            for i in range(int(rhsInt.toString()) - 1):
                bro._tail = bro._head
                while bro._tail.next != None:
                    bro._tail = bro._tail.next
                print('n', numb)
                numb = numb.arithmetic(bro, '*')
            return numb

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
    a = BigInteger(85)
    print(a)
    b = BigInteger(4)
    print(b)
    print(a.comparable(b))
    print(str(a.bitwise_ops(b, '^')))
    print(a.arithmetic(b, '**'))
