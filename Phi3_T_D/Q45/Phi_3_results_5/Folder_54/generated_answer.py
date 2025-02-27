from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    char_range = slice(4, 10)
    char_set = set(s[char_range].lower())
    if len(char_set) < 4:
        return set()
    found_palindromes = set()
    for perm_len in range(4, len(char_set) + 1):
        for perm in permutations(char_set, perm_len):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                found_palindromes.add(candidate)
    return found_palindromes