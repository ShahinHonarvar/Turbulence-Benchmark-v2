import itertools

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_between_indices(s):
    substring = s[4:10]
    letters = ''.join(sorted(set(substring), key=substring.index))
    combinations = set(itertools.permutations(letters, 5))
    palindromes = {''.join(p) for p in combinations if is_palindrome(''.join(p))}
    return palindromes