from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    middle_alphabet = s[3:6].lower()
    possible_words = set(permutations(middle_alphabet))
    palindromes = {''.join(p) for p in possible_words if is_palindrome(''.join(p))}
    return palindromes