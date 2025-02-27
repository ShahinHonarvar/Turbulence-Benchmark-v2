from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    sub_str = s[4:10]
    letters = ''.join(filter(str.isalpha, sub_str)).lower()
    permutations_gen = permutations(letters)
    palindromes = {''.join(p) for p in permutations_gen if is_palindrome(''.join(p))}
    return {p for p in palindromes if len(p) >= 3}