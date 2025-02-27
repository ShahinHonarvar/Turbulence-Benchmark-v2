from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    if len(s) < 7 or len(s) > 8:
        return set()
    letters_to_use = ''.join([c.lower() for c in s[1:8] if c in ascii_lowercase])
    if len(letters_to_use) < 5:
        return set()
    palindromes = set()
    for perm in set(permutations(letters_to_use, 5)):
        palindrome_candidate = ''.join(perm) + ''.join(perm[:-1][::-1])
        if is_palindrome(palindrome_candidate):
            palindromes.add(palindrome_candidate)
    return palindromes