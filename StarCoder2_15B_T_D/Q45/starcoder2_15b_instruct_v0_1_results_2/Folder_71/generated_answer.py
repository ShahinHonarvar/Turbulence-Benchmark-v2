import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    palindromes = set()
    letters = [c for c in s.lower() if c.isalpha()]
    for permutation in itertools.permutations(letters[1:4]):
        palindrome = ''.join(permutation)
        if is_palindrome(palindrome) and len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes