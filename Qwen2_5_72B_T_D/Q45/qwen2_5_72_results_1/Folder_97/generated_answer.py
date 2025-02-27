from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:5]
    letters = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for length in range(3, len(letters) + 1):
        for combo in permutations(letters, length):
            word = ''.join(combo)
            if word == word[::-1]:
                found_palindromes.add(word)
    return found_palindromes