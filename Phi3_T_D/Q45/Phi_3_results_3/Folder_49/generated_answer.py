import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    indices_range = s[5:8]
    letters = set(indices_range.lower())
    palindromes = set()
    for length in range(3, len(indices_range) + 1):
        for substring in itertools.permutations(letters, length):
            if is_palindrome(''.join(substring)):
                palindromes.add(''.join(substring))
    return palindromes