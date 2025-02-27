from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(input_string):
    start_index = 3
    end_index = 7
    substr = input_string[start_index:end_index + 1].lower()
    length = end_index - start_index + 1
    palindromes = set()
    chars = [char for char in sorted(substr) if char.isalpha()]
    for perm in set(permutations(chars, length)):
        s = ''.join(perm)
        if is_palindrome(s):
            palindromes.add(s)
    return palindromes