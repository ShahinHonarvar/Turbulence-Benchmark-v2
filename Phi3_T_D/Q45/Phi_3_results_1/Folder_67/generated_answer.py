from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7]
    possible_letters = ''.join(filter(str.isalpha, substring.lower()))
    if len(possible_letters) < 5:
        return set()
    palindromes = {''.join(p) for i in range(5, len(possible_letters) + 1) for p in permutations(possible_letters, i)}
    return {p for p in palindromes if p == p[::-1]}