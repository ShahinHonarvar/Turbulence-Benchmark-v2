from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = s[3:6].lower()
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes