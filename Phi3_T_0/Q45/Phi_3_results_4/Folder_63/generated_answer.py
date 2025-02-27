from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    s = s[0:4].lower()
    letters = ''.join(filter(str.isalpha, s))
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in permutations(letters, 3):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes