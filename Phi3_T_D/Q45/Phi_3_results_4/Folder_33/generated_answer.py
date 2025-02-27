from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    start, end = (6, 10)
    substring = s[start:end].lower()
    letters = ''.join(sorted(set(substring)))
    if len(letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in permutations(letters, length):
            palindrome_candidate = ''.join(p) + ''.join(reversed(p))
            if is_palindrome(palindrome_candidate):
                palindromes.add(palindrome_candidate)
    return palindromes