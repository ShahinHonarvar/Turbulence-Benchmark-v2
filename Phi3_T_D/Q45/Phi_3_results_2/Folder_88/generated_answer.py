from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    sub_str = s[3:8]
    letters = ''.join(filter(str.isalpha, sub_str)).lower()
    perms = [''.join(p) for p in permutations(letters)]
    palindromes = {perm for perm in perms if len(perm) >= 6 and is_palindrome(perm)}
    return palindromes