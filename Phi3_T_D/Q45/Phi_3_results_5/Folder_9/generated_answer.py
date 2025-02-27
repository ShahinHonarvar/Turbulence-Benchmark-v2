from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    prefix = s[:7].lower()
    letters = [char for char in prefix if char.isalpha()]
    permutations_list = [''.join(p) for p in permutations(letters)]
    palindromes_set = {word for word in permutations_list if is_palindrome(word)}
    return palindromes_set