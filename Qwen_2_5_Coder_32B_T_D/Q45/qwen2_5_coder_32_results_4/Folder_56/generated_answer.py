from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:10] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes