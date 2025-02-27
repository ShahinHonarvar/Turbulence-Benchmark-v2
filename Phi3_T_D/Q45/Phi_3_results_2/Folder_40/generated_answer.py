from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def get_characters_in_range(s, start, end):
        return s[start:end + 1].lower()
    characters = get_characters_in_range(s, 4, 9)
    permutations_set = set((''.join(p) for i in range(7, len(characters) + 1) for p in permutations(characters, i)))
    return {p for p in permutations_set if is_palindrome(p)}