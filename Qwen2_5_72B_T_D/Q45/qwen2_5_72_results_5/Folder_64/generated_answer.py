from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[4:10]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    possible_palindromes = set()
    for perm in permutations(letter_counts.elements()):
        perm_str = ''.join(perm)
        if len(perm_str) >= 5 and is_palindrome(perm_str):
            possible_palindromes.add(perm_str)
    return possible_palindromes