from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower() and len(word) >= 5
    substring = s[3:9]
    possible_chars = ''.join(filter(str.isalpha, substring)).lower()
    if len(possible_chars) < 5:
        return set()
    result = set()
    for length in range(5, len(possible_chars) + 1):
        for perm in permutations(possible_chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                result.add(word)
    return result