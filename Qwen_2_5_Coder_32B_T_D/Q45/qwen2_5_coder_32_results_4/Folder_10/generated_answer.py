import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:6] if c.isalpha()]
    palindromes = set()
    for length in range(3, 6):
        for perm in itertools.permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes