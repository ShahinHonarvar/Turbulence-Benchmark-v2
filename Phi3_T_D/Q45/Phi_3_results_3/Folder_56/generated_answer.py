from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[4:10].lower()
    possible_chars = [''.join(p) for i in range(5, 10) for p in permutations(sub_str, i) if p == p[::-1]]
    return set(dict.fromkeys(possible_chars))