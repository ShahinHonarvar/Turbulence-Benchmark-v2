import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:10] if char.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for combo in itertools.permutations(letters, length):
            word = ''.join(combo)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes