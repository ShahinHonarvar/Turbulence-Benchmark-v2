from itertools import permutations

def is_palindrome(word):
    return word == word[::-1]

def palindromes_between_indices(string):
    subset = string[3:10]
    palindromes = set()
    for length in range(7, len(subset) + 1):
        for perm in permutations(subset, length):
            candidate = ''.join(perm).lower()
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes