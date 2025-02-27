from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    letters = sorted(filter(str.isalpha, s[:4].lower()))
    palindromes = set()
    if len(letters) < 4:
        return palindromes
    for p in permutations(letters, 4):
        word = ''.join(p)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes