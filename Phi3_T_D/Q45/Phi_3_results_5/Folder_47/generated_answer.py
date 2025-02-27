from itertools import permutations

def palindromes_between_indices(s):
    subset = s[3:8].lower()

    def is_palindrome(word):
        return word == word[::-1]
    unique_chars = sorted(set(subset))
    palindromes = set()
    for length in range(5, len(unique_chars) + 1):
        for combo in permutations(unique_chars, length):
            word = ''.join(combo)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes