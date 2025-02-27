from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    subset = s[0:3]
    subset = ''.join(filter(str.isalpha, subset)).lower()
    unique_chars = set(subset)
    palindrome_set = set()
    for length in range(3, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindrome_set.add(perm_str)
    return palindrome_set