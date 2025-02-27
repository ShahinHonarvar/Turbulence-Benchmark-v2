from itertools import permutations

def palindromes_between_indices(s):
    letters = s[2:8]
    letters = ''.join(filter(str.isalpha, letters))
    letters = letters.lower()
    unique_letters = set(letters)
    palindromes = set()
    for r in range(3, len(unique_letters) + 1):
        for p in permutations(unique_letters, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes