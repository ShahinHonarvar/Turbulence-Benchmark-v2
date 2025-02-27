from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    chars_between = s[1:9]
    permutations_list = set((''.join(p) for p in permutations(chars_between)))
    return {p for p in permutations_list if is_palindrome(p) and len(p) >= 4}