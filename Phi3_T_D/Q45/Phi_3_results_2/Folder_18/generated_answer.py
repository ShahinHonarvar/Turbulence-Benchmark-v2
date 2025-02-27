from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    sub_str = s[1:7]
    chars = [c.lower() for c in sub_str if c.isalpha()]
    unique_chars = set(chars)
    palindromes = set()
    for perm in permutations(unique_chars, len(unique_chars)):
        candidate = ''.join(perm)
        if len(candidate) >= 3 and is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes