from node import *

# A class implementing Multiset as a linked list.


class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head is None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        """

        :return:
        """
        self._head = None

    def __len__(self):
        nd_temp = self._head
        res = 0
        while nd_temp is not None:
            res += 1
            nd_temp = nd_temp.next
            if nd_temp == self._head:
                break
        return res


    def split_half(self):
        """

        :return:
        """
        nd_halfer = self._head
        mult1 = Multiset()
        mult2 = Multiset()
        id = 0
        half_pos = len(self) // 2
        while id < len(self):
            if id < half_pos:
                mult1.add(nd_halfer)
            else:
                mult2.add(nd_halfer)
            id += 1
            nd_halfer = nd_halfer.next
        print('1')
        print(mult1)
        print('2')
        print(mult2)
        return mult1, mult2

    def __str__(self):
        ndnd = self._head
        words = ''
        while ndnd is not None:
            words += str(ndnd)
            words += "\n"
            ndnd = ndnd.next
        return words

if __name__ == "__main__":
    m = Multiset()
    m.add(123)
    m.add("adsa")
    m.add("rer")
    m.add("QWE")
    m.add(999)
    print(m._head)
    print(m)
    m.split_half()
