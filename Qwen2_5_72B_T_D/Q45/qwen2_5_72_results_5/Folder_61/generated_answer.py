from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:8]
    all_chars = [ch.lower() for ch in substring if ch.isalpha()]
    found_palindromes = set()
    for perm in permutations(all_chars, 7):
        word = ''.join(perm)
        if word == word[::-1]:
            found_palindromes.add(word)
    return found_palindromes