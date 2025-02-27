from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    substring = s[2:5]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes