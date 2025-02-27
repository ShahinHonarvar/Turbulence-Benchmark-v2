import itertools

def palindromes_between_indices(s):
    letters = s[3:7].lower()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            word = ''.join(combo)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes