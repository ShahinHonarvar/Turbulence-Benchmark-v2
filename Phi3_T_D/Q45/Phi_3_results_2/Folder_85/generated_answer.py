from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    min_length = 7
    start, end = (2, 8)
    substring = s[start - 1:end]
    alphabet_set = set(ascii_lowercase)
    eligible_chars = ''.join([char.lower() for char in substring if char.lower() in alphabet_set])
    if len(eligible_chars) < min_length:
        return set()
    unique_combinations = set()
    for length in range(min_length, len(eligible_chars) + 1):
        for perm in permutations(eligible_chars, length):
            unique_combinations.add(''.join(perm))
    palindrome_set = {word for word in unique_combinations if is_palindrome(word)}
    return palindrome_set