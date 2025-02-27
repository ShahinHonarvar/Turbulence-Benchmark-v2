from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    alphanumeric_chars = [char.lower() for char in s[4:7] if char.isalpha()]
    distinct_chars = ''.join(set(alphanumeric_chars))
    palindromes = set()
    for perm in permutations(distinct_chars, 4):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes