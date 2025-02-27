from itertools import permutations

def palindromes_between_indices(s):
    start, end = (2, 9)
    substring = s[start:end + 1].lower()
    unique_letters = set(substring)
    results = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(4, len(substring) + 1):
        for perm in permutations(unique_letters, length):
            word = ''.join(perm)
            if is_palindrome(word) and word in substring:
                results.add(word)
    return results