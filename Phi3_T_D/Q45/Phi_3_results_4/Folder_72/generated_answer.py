import itertools

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindromes_between_indices(s: str) -> set:
    substring = s[1:8].lower()
    palindromes = set()
    for length in range(6, len(substring) + 1):
        for permutation in itertools.permutations(substring, length):
            palindrome_candidate = ''.join(permutation)
            if is_palindrome(palindrome_candidate):
                palindromes.add(palindrome_candidate)
    return palindromes