from itertools import permutations

def palindromes_between_indices(input_str):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set([c.lower() for c in input_str[2:8] if c.isalpha()])
    permutations_list = set([''.join(p) for p in permutations(letters, 4)])
    return {word for word in permutations_list if is_palindrome(word)}