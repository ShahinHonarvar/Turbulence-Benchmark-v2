from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(input_string):
    substring = input_string[3:8].lower()
    unique_chars = ''.join(set(substring))
    palindrome_set = set()
    for length in range(5, len(substring) + 1):
        for perm in permutations(unique_chars, length):
            if is_palindrome(''.join(perm)):
                palindrome_set.add(''.join(perm))
    return palindrome_set