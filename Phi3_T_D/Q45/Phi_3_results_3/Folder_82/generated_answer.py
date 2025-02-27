from itertools import permutations

def palindromes_between_indices(s):
    letters_only = ''.join(filter(str.isalpha, s[1:7].lower()))
    unique_letters = ''.join(set(letters_only))
    if len(unique_letters) >= 7:
        perms = set((''.join(p) for p in permutations(unique_letters, 7)))
        palindromes = {word for word in perms if word == word[::-1]}
    else:
        palindromes = set()
    return palindromes