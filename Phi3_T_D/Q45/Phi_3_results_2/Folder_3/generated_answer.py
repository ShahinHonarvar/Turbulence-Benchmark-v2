from itertools import permutations

def palindromes_between_indices(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    string_slice = input_string[6:10]
    letters = ''.join(filter(str.isalpha, string_slice)).lower()
    if len(letters) < 2:
        return set()
    palindromes = set((''.join(p) for p in permutations(letters, 2) + (''.join(p) for p in permutations(letters, len(letters)))))
    return {p for p in palindromes if is_palindrome(p)}