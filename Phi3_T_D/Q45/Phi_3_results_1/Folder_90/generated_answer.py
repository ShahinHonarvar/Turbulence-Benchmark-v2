import itertools

def is_palindrome(s):
    return s.lower() == s[::-1].lower() and len(s) >= 4

def palindromes_between_indices(s):
    substring = s.lower()[0:6]
    letters = set(substring)
    palindromes = set()
    for length in range(4, len(substring) + 1):
        for perm in itertools.permutations(letters, length):
            palindrome_candidate = ''.join(perm).ljust(length, perm[-1])
            if is_palindrome(palindrome_candidate):
                palindromes.add(palindrome_candidate)
    return palindromes