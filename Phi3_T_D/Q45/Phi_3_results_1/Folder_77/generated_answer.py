from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(text):
    chars_in_range = text[3:7]
    palindromes = set()
    for length in range(4, len(chars_in_range) + 1):
        for perm in permutations(chars_in_range, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes