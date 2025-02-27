from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(s):
        return s == s[::-1]
    letters = sorted(set(text[:8].lower()))
    length = 7
    palindromes = set()
    for subset in permutations(letters, length):
        palindrome_candidate = ''.join(subset) + ''.join(reversed(subset))
        if is_palindrome(palindrome_candidate):
            palindromes.add(palindrome_candidate)
    return palindromes