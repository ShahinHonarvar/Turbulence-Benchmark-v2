from itertools import permutations

def is_palindrome(word):
    return word == word[::-1]

def palindromes_between_indices(s):
    sub_str = s[2:6].lower()
    unique_chars = set(sub_str)
    palindromes = set()
    if len(unique_chars) < 3:
        return palindromes
    for length in range(3, len(sub_str) + 1):
        for perm in permutations(unique_chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes