from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(s):
    letters = ''.join([ch for ch in s[:7] if ch in ascii_letters]).lower()
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes