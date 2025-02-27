from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[2:10].lower()

    def is_palindrome(s):
        return s == s[::-1]
    unique_chars = sorted(set(sub_str))
    palindromes = {''.join(p) for p in permutations(unique_chars, 7)}
    return {p for p in palindromes if is_palindrome(p)}