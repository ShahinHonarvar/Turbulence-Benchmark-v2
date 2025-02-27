from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:7].lower()
    letter_permutations = set([''.join(p) for p in permutations(substring)])
    palindromes = {word for word in letter_permutations if word == word[::-1] and len(word) >= 4}
    return palindromes