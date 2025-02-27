from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    s_lower = s.lower()
    letters = [c for c in s_lower[0:8] if c.isalpha()]
    palindromes = set()
    for length in range(6, 9):
        for p in permutations(letters, length):
            word = ''.join(p)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes