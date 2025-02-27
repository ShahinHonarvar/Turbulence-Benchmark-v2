from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(input_string):
    alphabet_subset = input_string[:6].lower()
    unique_letters = ''.join(set(alphabet_subset))
    if len(unique_letters) < 6:
        return set()
    permutations_set = set([''.join(p) for p in permutations(unique_letters, 6)])
    palindromes = {s for s in permutations_set if is_palindrome(s)}
    return palindromes