from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    start, end = (4, 9)
    substring = s[start:end + 1]
    letters_count = {}
    for char in substring:
        char_lower = char.lower()
        if char_lower.isalpha():
            letters_count[char_lower] = letters_count.get(char_lower, 0) + 1
    possible_palindromes = set()
    for length in range(7, len(substring) + 1):
        for perm in permutations(letters_count.keys(), length):
            conf_perm = ''.join(perm)
            if is_palindrome(conf_perm):
                possible_palindromes.add(conf_perm)
    return possible_palindromes