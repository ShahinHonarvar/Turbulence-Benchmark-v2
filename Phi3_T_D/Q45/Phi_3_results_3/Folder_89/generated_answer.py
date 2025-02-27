from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    char_range = s[5:10]
    perms = set([''.join(p) for p in permutations(char_range) if len(p) >= 6])
    result = set(filter(is_palindrome, perms))
    return result