from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:10])).lower()
    p = set([''.join(x) for x in permutations(letters)])
    palindromes = {word for word in p if len(word) >= 5 and word == word[::-1]}
    return palindromes