from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10]
    for length in range(5, len(substring) + 1):
        for perm in permutations(substring.lower()):
            word = ''.join(perm)
            if word == word[::-1]:
                yield word

def get_palindromes(s):
    return set(palindromes_between_indices(s))