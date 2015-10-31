import random

__author__ = 'gal'


def get_primes(n):
    res = []
    for num in range(2, n):
        flag = True
        for divider in range(2, num):
            if num % divider == 0:
                flag = False
                continue
        if flag:
            res.append(num)
    return res


print "primes to 40: %s" % get_primes(40)


def get_string_lengths(str_list):
    res = []
    for s in str_list:
        res.append(len(s))
    return res

print "strings lengths: %s" % get_string_lengths(["abra kadabra", "blabla", "foo_foo"])


def get_avg_string_length(str_list):
    lengths = get_string_lengths(str_list)
    return sum(lengths) / float(len(lengths))

print "avg strings lengths: %s" % get_avg_string_length(["abra kadabra", "blabla", "foo_foo"])

scissors = 0
paper = 1
rock = 2
lizard = 3
spock = 4


def rock_paper_scissors(player1, player2):
    if (player1 == scissors and player2 == paper) or (player1 == rock and player2 == scissors):
        return "Win"
    elif player1 == player2:
        return "Draw"
    else:
        return "Lose"

print "player 1 %s rock_paper_scissors" % rock_paper_scissors(rock, scissors)


def rock_paper_scissors_lizard_spock(player1, player2):
    if (player1 == scissors and player2 == paper) or (player1 == rock and player2 == scissors)\
            or (player1 == scissors and player2 == lizard) or (player1 == lizard and player2 == spock):
        return "Win"
    elif player1 == player2:
        return "Draw"
    else:
        return "Lose"

print "player 1 %s rock_paper_scissors_lizard_spock" % rock_paper_scissors_lizard_spock(spock, lizard)


def generate_brackets(size):
    rand_bin_list = lambda n: [random.randint(0,1) for b in range(1,n+1)]
    l = rand_bin_list(size)
    for i, n in enumerate(l):
        if n == 0:
            l[i] = "["
        else:
            l[i] = "]"
    return ''.join(l)

brackets_str = generate_brackets(10)
print "brackets list: %s" % brackets_str


def check_balanced_brackets():
    brackets_list = list(brackets_str)
    stack = []

    if len(brackets_list) % 2 != 0:
        return False
    for b in brackets_list:
        if b == "[":
            stack.append("[")
        else:
            if len(stack) > 0:
                stack.pop()
    return len(stack) < 1

print "brackets balanced: %s" % check_balanced_brackets()

