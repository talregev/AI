from random import randint


lfib = lambda n: \
                 [0] if n == 0 else \
                 [0,1] if n == 1 else \
                 lfib(n-1) + [lfib(n-2)[-2] + lfib(n-1)[-1]] \
                 if len(lfib(n-2)) == len(lfib(n-1)) and (lfib(n-2)[-2] + lfib(n-1)[-1]) <= n else\
                 lfib(n-1) if len(lfib(n-2)) == len(lfib(n-1)) and (lfib(n-2)[-2] + lfib(n-1)[-1]) > n else \
                 lfib(n-1) + [lfib(n-2)[-1] + lfib(n-1)[-1]] if (lfib(n-2)[-1] + lfib(n-1)[-1]) <= n else \
                 lfib(n-1)

isPrime = lambda n,x:  False if n < 2 else \
                       True  if n == 2 else \
                       False  if (x == 2 and n % x == 0) else \
                       True if (x == 2 and n % x != 0) else \
                       isPrime(n,x-1) if (x == n) else \
                       n % x != 0 and isPrime(n,x-1) 

lprime = lambda n: \
            [] if n < 2 else \
            lprime(n-1) + [n]  if isPrime(n,n) else lprime(n-1)


def list_prime(n):
    prime_list = []
    if n < 2:
        return
    for p in range(2,n+1):
        if (is_prime(p)):
            prime_list.append(p)
    return prime_list

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i=5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def list_fib(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0,1]
    fibValues = [0,1]
    i=2
    while fibValues[i-1] + fibValues[i-2] <= n:       
        fibValues.append(fibValues[i-1] + fibValues[i-2])
        i = i + 1
    return fibValues

def num_words(st):
    numbers = []
    words = st.split()
    for word in words:
        numbers.append(len(word))
    return numbers

def avg_num_words(st):
    numbers = num_words(st)
    sum = 0
    for number in numbers:
        sum = sum + number
    return float(sum) / len(numbers)


def enum(**enums):
    return type('Enum', (), enums)

Game = enum(Scissors=0, Paper=1, Rock=2, Lizard=3, Spock=4)

def RockPaperScissors(first, second):
    if (first < 0 or first > 2 or second < 0 or second > 2):
        raise Exception("Illegal move") 
    if (first == second):
        return "Draw"
    switcher = {
        0: ["Draw", "Win", "Lose"],
        1: ["Lose", "Draw", "Win"],
        2: ["Win", "Lose", "Draw"],
    }
    switcher2 = switcher.get(first, "nothing")
    return switcher2[second]

    

def RockPaperScissorsLizardSpock(first, second):
    if (first < 0 or first > 4 or second < 0 or second > 4):
        raise Exception("Illegal move") 
    if (first == second):
        return "Draw"
    switcher = {
        0: ["Draw", "Win",  "Lose", "Win",  "Lose"],
        1: ["Lose", "Draw", "Win",  "Lose", "Win"],
        2: ["Win",  "Lose", "Draw", "Win",  "Lose"],
        3: ["Lose", "Win",  "Lose", "Draw", "Win"],
        4: ["Win",  "Lose", "Win",  "Lose", "Draw"],
    }
    switcher2 = switcher.get(first, "nothing")
    return switcher2[second]

def random_brackets(n):
    numOpen     = 0
    numClose    = 0
    string      = ""
    for i in range (0,n*2):
        if (numOpen >= n):
            string      += "]"
            numClose    += 1
            continue
        if (numClose >= n):
            string      += "["
            numOpen     += 1
            continue
        isClose = randint(0,1)
        if(isClose):
            string      += "]"
            numClose    += 1
        else:
            string      += "["
            numOpen     += 1
    return string
            
def random_balanced_brackets(n):
    brackets    = [] 
    string      = ""   
    num_opening = 0
    for i in range (0,n*2):
        if num_opening >= n:
            string += "]"
            brackets.remove("[")
            continue;
        #List is empty
        if not brackets:
            string += "["
            brackets.append("[")
            num_opening += 1
            continue;
        isClose = randint(0,1)
        if(isClose):
            string += "]"
            brackets.remove("[")
        else:
            string += "["
            brackets.append("[")
            num_opening += 1
    return string

def is_balanced(string):
    brackets    = []
    numOpen     = 0
    numClose    = 0
    for char in string:
        if char == '[':
            brackets.append("[")
            numOpen += 1
            continue;
        #List is empty
        if not brackets:
            return "NOT OK"
        brackets.remove("[")
        numClose += 1
    if numClose == numOpen:
        return "OK"
    return "NOT OK"
        
if __name__ == "__main__":
    print list_prime(1000)
    print list_fib(1000)
    print num_words("Tal Regev is the best")
    print avg_num_words("Tal Regev is the best")
    print RockPaperScissors(Game.Paper,Game.Rock)
    print RockPaperScissorsLizardSpock(Game.Spock,Game.Rock)
    string1 = random_balanced_brackets(10)    
    string2 = random_brackets(10)
    print "random_balanced_brackets",string1
    print "random_brackets",string2
    print is_balanced(string1)
    print is_balanced(string2)
    #print lfib(12)
    print lprime(100)


