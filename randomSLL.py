import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertEnd(self,val):
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
            return
        self.tail.next = node
        self.tail = node

# random => start to end both included with count = 1
def randSLL(start:int, end:int, count:int = 1):
    sll = SLL()
    for _ in range(count):
        rval = random.randint(start,end)
        sll.insertEnd(rval)
    return sll.head

# random => start to end both included odd count = 1
def randOddSLL(start:int, end:int, count:int = 1):
    sll = SLL()
    while count>0:
        rval = random.randint(start,end)
        if rval%2!=0:
            sll.insertEnd(rval)
            count-=1
    return sll.head

# random => start to end both included odd count = 1
def randEvenSLL(start:int, end:int, count:int = 1):
    sll = SLL()
    while count>0:
        rval = random.randint(start,end)
        if rval%2==0:
            sll.insertEnd(rval)
            count-=1
    return sll.head

# random => PRIME count = 1
def isPrime(n:int):
    if n<=3 and n>1:
        return 1
    if n%2==0 or n%3==0:
        return 0
    i=5
    while i*i<n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True

def randPrimeSLL(start:int, end:int, count:int = 1):
    arr = []
    sll = SLL()
    for i in range(start,end+1):
        pval = i
        if pval<0:
            pval*=-1
        if isPrime(pval):
            arr.append(i)
    for _ in range(count):
        sll.insertEnd(random.choice(arr))
    return sll.head

def randAlphaSLL(type:str, count:int = 1):
    LCASE = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    sll = SLL()
    if type == "UPPER":
        for _ in range(count):
            sll.insertEnd(random.choice(LCASE).upper())
    elif type == "LOWER":
        for _ in range(count):
            sll.insertEnd(random.choice(LCASE))
    elif type == "MIXED":
        for _ in range(count):
            rval = random.choice(LCASE)
            if random.choice([True,False]):
                rval = rval.upper()
            sll.insertEnd(rval)
    return sll.head