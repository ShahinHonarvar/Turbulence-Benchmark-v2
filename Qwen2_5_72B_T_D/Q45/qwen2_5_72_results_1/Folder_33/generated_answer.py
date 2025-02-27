from itertools import permutations

def palindromes_between_indices(s):
    substring = s[7:10]
    letters = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 4):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes