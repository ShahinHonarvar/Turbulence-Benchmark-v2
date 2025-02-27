from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters = set(s[2:9].lower())
    palindromes = set()
    for permutation in permutations(letters):
        palindrome = ''.join(permutation)
        if is_palindrome(palindrome) and len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes