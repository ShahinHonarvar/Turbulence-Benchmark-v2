from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(string):
        return string == string[::-1]
    alpha_chars = [char.lower() for char in text[2:7] if char.isalpha()]
    unique_combinations = set(permutations(alpha_chars))
    palindromes = set((''.join(comb) for comb in unique_combinations if is_palindrome(''.join(comb))))
    return {''.join(palindrome).capitalize() for palindrome in palindromes if len(palindrome) >= 3}