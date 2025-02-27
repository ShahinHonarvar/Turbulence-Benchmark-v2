from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    substr = s[1:10].lower()
    unique_chars = ''.join(sorted(set(substr)))
    valid_palindromes = {''.join(p) for p in permutations(unique_chars) if len(p) >= 7 and is_palindrome(''.join(p))}
    return valid_palindromes