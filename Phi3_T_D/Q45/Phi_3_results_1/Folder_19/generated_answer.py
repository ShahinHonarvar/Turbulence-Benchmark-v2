from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    subsequence = s[1:8]
    letters_set = set(subsequence.lower())
    valid_letters = [letter for letter in letters_set if letter.isalpha()]
    if len(valid_letters) < 7:
        return set()
    all_permutations = {''.join(k) for i in range(7, len(valid_letters) + 1) for k in permutations(valid_letters, i)}
    return {p for p in all_permutations if is_palindrome(p)}