from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = [c.lower() for c in s[4:9]]
    palindromes = set()
    for perm in permutations(letters, 6):
        candidate = ''.join(perm)
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes