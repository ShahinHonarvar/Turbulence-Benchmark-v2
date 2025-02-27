from itertools import permutations

def palindromes_between_indices(s):
    selected_chars = [c.lower() for c in s[3:9]]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for word_length in range(5, len(selected_chars) + 1):
        for perm in permutations(selected_chars, word_length):
            perm_str = ''.join(perm).lower()
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes