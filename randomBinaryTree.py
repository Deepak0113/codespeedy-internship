import random

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return

        q = []
        q.append(self.root)
        while len(q):
            temp = q[0]
            q.pop(0)

            if not temp.left:
                temp.left = Node(val)
                break
            q.append(temp.left)
            
            if not temp.right:
                temp.right = Node(val)
                break
            q.append(temp.right)

def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.val,end = " ")
    inorder(temp.right)

# random => start to end both included with count = 1
def randBT(start:int, end:int, count:int = 1):
    bt = BT()
    for _ in range(count):
        rval = random.randint(start,end)
        bt.insert(rval)
    return bt.root

# random => start to end both included odd count = 1
def randOddBT(start:int, end:int, count:int = 1):
    bt = BT()
    while count>0:
        rval = random.randint(start,end)
        if rval%2!=0:
            bt.insert(rval)
            count-=1
    return bt.root

# random => start to end both included odd count = 1
def randEvenBT(start:int, end:int, count:int = 1):
    bt = BT()
    while count>0:
        rval = random.randint(start,end)
        if rval%2==0:
            bt.insert(rval)
            count-=1
    return bt.root

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

def randPrimeBT(start:int, end:int, count:int = 1):
    arr = []
    bt = BT()
    for i in range(start,end+1):
        pval = i
        if pval<0:
            pval*=-1
        if isPrime(pval):
            arr.append(i)
    for _ in range(count):
        rval = random.choice(arr)
        bt.insert(rval)
    return bt.root

# random => alphabets UPPER LOWER MIXED with count = 1
def randAlphaBT(type:str, count:int = 1):
    LCASE = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    bt = BT()
    l=[]
    if type == "UPPER":
        for _ in range(count):
            rval = random.choice(LCASE).upper()
            bt.insert(rval)
            l.append(rval)
    elif type == "LOWER":
        for _ in range(count):
            rval = random.choice(LCASE)
            bt.insert(rval)
            l.append(rval)
    elif type == "MIXED":
        for _ in range(count):
            rval = random.choice(LCASE)
            if random.choice([True,False]):
                rval = rval.upper()
            bt.insert(rval)
            l.append(rval)
    return bt.root

