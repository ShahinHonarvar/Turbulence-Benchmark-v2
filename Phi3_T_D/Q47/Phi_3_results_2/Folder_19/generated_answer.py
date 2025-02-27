from itertools import combinations

def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    s = s[10:56]
    found_palindromes = set()
    for length in range(3, 8):
        for start_index in range(0, len(s) - length + 1):
            candidate = s[start_index:start_index + length]
            if all((c.isalpha() for c in candidate)) and is_palindrome(candidate):
                found_palindromes.add(candidate)
    return found_palindromes