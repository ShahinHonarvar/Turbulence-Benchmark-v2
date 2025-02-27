from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    sub_text = text[1:7].lower()
    used_chars = set(sub_text)
    palindromes = {''.join(p) for p in permutations(sub_text) if is_palindrome(''.join(p)) and len(p) >= 4}
    return palindromes