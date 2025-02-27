from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    for word_length in range(4, 7):
        for perm in permutations(s[0:7].lower(), word_length):
            word = ''.join(perm)
            if is_palindrome(word):
                yield word