from itertools import permutations

def palindromes_between_indices(s):
    subset = s[6:10]
    subset = subset.lower()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    sub_list = [char for char in subset if char in english_letters]

    def is_palindrome(s):
        return s == s[::-1]
    possible_permutations = {''.join(p) for i in range(3, len(sub_list) + 1) for p in permutations(sub_list, i)}
    palindromes = {p for p in possible_permutations if is_palindrome(p)}
    return palindromes