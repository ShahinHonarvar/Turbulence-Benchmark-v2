from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def get_digits(s, start, end):
    return set(s[start:end + 1].lower())

def get_strings(chars, length):
    for combination in permutations(chars, length):
        yield ''.join(combination)

def palindromes_between_indices(s):
    start, end = (2, 5)
    digits = get_digits(s, start, end)
    palindromes = set()
    for length in range(4, len(digits) + 1):
        for s in get_strings(digits, length):
            if is_palindrome(s):
                palindromes.add(s)
    return palindromes