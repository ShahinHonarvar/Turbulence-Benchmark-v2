from itertools import permutations

def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

def palindromes_between_indices(text):
    substring = text[:7]
    palindromes = set()
    for i in range(3, len(substring) + 1):
        for perm in set(permutations(substring, i)):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes