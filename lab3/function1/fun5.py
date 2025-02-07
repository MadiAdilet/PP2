from itertools import permutations

def string_permutations(s):
    perms = [''.join(p) for p in permutations(s)]
    print(perms)

string_permutations("abc")