class Tree:
    def __init__(self, zero = None, one = None, *, unpack = None):
        if unpack:
            if type(unpack[0]) is tuple:
                self.zero = Tree(unpack = unpack[0])
            else:
                self.zero = unpack[0]
            
            if type(unpack[1]) is tuple:
                self.one = Tree(unpack = unpack[1])
            else:
                self.one = unpack[1]
                
        else:
            self.zero = zero
            self.one = one

    def add_zero(self, zero):
        self.zero = zero

    def add_one(self, zero):
        self.one = one

    def __str__(self):
        return f'Tree(0 = {self.zero}, 1 = {self.one})'


print(Tree(unpack = (
    ( ( ( ( 'Y', 'G'), ('U', 'M') ), 'T' ), (  ) ), ()
)))
    
