from itertools import permutations

def palindromes_between_indices(s):
    letters = s[6:10]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes