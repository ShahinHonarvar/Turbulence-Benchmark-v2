from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(s):
    substring = s[:4].lower()
    unique_letters = set(substring)
    results = set()
    for i in range(len(substring), 0, -1):
        for p in set(permutations(unique_letters, i)):
            palindrome_candidate = ''.join(p)
            if len(palindrome_candidate) >= 3 and is_palindrome(palindrome_candidate):
                results.add(palindrome_candidate)
    return results