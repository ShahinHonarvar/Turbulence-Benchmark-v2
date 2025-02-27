from itertools import permutations

def palindromes_between_indices(s):
    target_index_range = slice(1, 9)
    chars = s[target_index_range].lower()

    def is_palindrome(word):
        return word == word[::-1]
    unique_chars = set(chars)
    palindromes = set()
    for length in range(4, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes