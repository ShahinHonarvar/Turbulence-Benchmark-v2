from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    substr = s[1:4]
    chars = set(substr.lower())
    possible_palindromes = set()
    for perm in permutations([c for c in chars if c.isalpha()]):
        possible_palindrome = ''.join(perm)
        if is_palindrome(possible_palindrome) and len(possible_palindrome) >= 4:
            possible_palindromes.add(possible_palindrome)
    return possible_palindromes