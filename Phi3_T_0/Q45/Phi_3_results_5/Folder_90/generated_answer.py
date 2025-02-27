from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[:6].lower()
    letters = ''.join(filter(str.isalpha, s))
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in set(permutations(letters, 4)):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes