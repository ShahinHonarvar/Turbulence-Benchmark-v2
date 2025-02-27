from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    letters = s[0:9].lower()
    palindromes = set()
    for perm in permutations(letters, 7):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes