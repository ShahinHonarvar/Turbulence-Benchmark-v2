from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    letters = [c.lower() for c in s[:8]]
    result_set = set()
    for permutation in permutations(letters, 4):
        word = ''.join(permutation)
        if is_palindrome(word):
            result_set.add(word)
    return result_set