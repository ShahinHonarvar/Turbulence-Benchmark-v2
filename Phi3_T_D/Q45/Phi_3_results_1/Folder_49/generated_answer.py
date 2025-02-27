from itertools import permutations

def palindromes_between_indices(text):
    substr = text[5:8]

    def is_palindrome(s):
        return s == s[::-1]
    letters_between = set(substr.lower())
    palindromes = set()
    for length in range(3, len(letters_between) + 1):
        for perm in permutations(letters_between, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes