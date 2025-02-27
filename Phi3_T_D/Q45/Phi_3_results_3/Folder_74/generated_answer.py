from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    char_list = sorted([char.lower() for char in s[1:7] if char.isalpha()], key=lambda x: x.lower())
    distinct_chars = set(''.join(char_list))
    if len(distinct_chars) < 3:
        return set()
    palindrome_set = {''.join(p) for p in permutations(distinct_chars, 3)}
    return {p for p in palindrome_set if is_palindrome(p)}