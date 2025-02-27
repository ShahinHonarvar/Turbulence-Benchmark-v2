from itertools import product

def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s_in_range = s[40:95]
    eng_letters = set('abcdefghijklmnopqrstuvwxyz')
    return {word.lower() for word in (''.join(combo) for combo in product(s_in_range, repeat=l)) if all((c in eng_letters for c in word)) and 45 <= len(word) <= 51 and is_palindrome(word)}