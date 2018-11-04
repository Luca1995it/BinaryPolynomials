import copy

class BinPolynomial:
    ## BUILT-IN
    def __init__(self, array=[]):
        self.bits = array
        self.clean()

    def __len__(self):
        self.clean()
        return len(self.bits)

    def __str__(self):
        res = []
        for i in range(len(self)):
            if self.bits[i]:
                if i > 0:
                    res.append('x^%d' % i)
                else:
                    res.append('1')
        if not res:
            res = ['0']
        return '+'.join(res)

    def __iter__(self):
        return self.bits

    ## OPERATIONS
    def __add__(self, other):
        max_len = max(len(self), len(other))
        res = BinPolynomial()
        for i in range(max_len):
            res[i] = self[i] != other[i]
        return res

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        res = BinPolynomial()
        for i in range(len(self)):
            if self[i]:
                for j in range(len(other)):
                    if other[j]:
                        res[i+j] = res[i+j] != True
        return res

    def __rmul__(self, other):
        return self.__mul__(other)

    def __delitem__(self, key):
        self.bits[key] = False
        self.clean()

    def __setitem__(self, key, value):
        if key >= len(self):
            self.bits = self.bits + [False] * (1 + key - len(self))
        self.bits[key] = bool(value)
        self.clean()

    def __getitem__(self, key):
        if isinstance(key, slice):
            raise NotImplementedError()

        if key >= len(self):
            return False
        else:
            return self.bits[key]

    def deg(self):
        self.clean()
        return len(self)-1

    def mod(self, divisor):
        quotient = BinPolynomial()
        rest = copy.deepcopy(self)
        while rest.deg() >= divisor.deg():
            actual = rest.deg()-divisor.deg()
            quotient[actual] = 1
            for i in range(len(divisor)):
                if divisor[i]:
                    rest[i+actual] = rest[i+actual] != True
        return (quotient, rest)

    def __mod__(self, other):
        return self.mod(other)[1]

    def __truediv__(self, other):
        return self.mod(other)[0]

    def __eq__(self, other):
        return self.bits == other.bits

    def __ne__(self, other):
        return self.bits != other.bits

    def __pow__(self, p):
        if not isinstance(p, int):
            raise NotImplementedError()
        res = BinPolynomial([1])
        for x in range(p):
            res = res * self
        return res

    def __hash__(self):
        self.clean()
        return hash(tuple(self.bits))

    ## CLEANING
    def clean(self):
        last_one = 0
        for i in range(len(self.bits)):
            if self.bits[i]:
                last_one = i
        self.bits = [True if x else False for x in self.bits[:last_one+1]]

    ## GETTERS AND SETTERS
    def bin(self, s):
        return str(s) if s<=1 else self.bin(s>>1) + str(s&1)

    def from_int(self, number):
        self.bits = [bool(int(x)) for x in self.bin(number)]
        self.bits.reverse()
        self.clean()

    def get(self):
        self.clean()
        return self.bits
