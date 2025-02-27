from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = s[2:10].lower()
    unique_letters = ''.join(sorted(set(letters)))
    all_perms = set((''.join(p) for p in permutations(unique_letters, 4)))
    palindromes = {p for p in all_perms if is_palindrome(p)}
    return palindromes