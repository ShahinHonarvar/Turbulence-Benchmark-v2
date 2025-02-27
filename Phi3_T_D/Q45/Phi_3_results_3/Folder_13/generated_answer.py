import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[3:10].lower()
    letters = set(s)
    palindromes = set()
    for length in range(5, len(s) + 1):
        for permutation in itertools.permutations(letters, length):
            permutation_string = ''.join(permutation)
            if is_palindrome(permutation_string):
                palindromes.add(permutation_string)
    return palindromes