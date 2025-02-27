from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(s):
    charset = {char.lower() for char in s[:8] if char.isalpha()}
    palindromes = set()
    for length in range(7, 8):
        for perm in permutations(charset, length):
            palindrome_candidate = ''.join(perm).lower()
            if is_palindrome(palindrome_candidate):
                palindromes.add(palindrome_candidate)
    return palindromes