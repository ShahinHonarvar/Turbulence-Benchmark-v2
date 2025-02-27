from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[0:4].lower()
    letters = set(s)
    palindromes = set()
    for length in range(3, len(s) + 1):
        for perm in permutations(s, length):
            if is_palindrome(''.join(perm)):
                palindromes.add(''.join(perm))
    return palindromes