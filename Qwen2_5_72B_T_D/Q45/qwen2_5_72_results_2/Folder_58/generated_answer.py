from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7].lower()
    chars = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(chars, 6):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes