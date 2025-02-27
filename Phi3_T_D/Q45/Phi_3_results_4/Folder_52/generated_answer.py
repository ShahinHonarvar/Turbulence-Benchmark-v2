import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[:8].lower()
    letters = ''.join(filter(str.isalpha, substring))
    if len(letters) < 6:
        return set()
    palindrome_set = set()
    for k in range(6, len(letters) + 1):
        for subset in itertools.permutations(letters, k):
            s = ''.join(subset)
            if is_palindrome(s):
                palindrome_set.add(s)
    return palindrome_set