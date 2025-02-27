from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    mid = s[1:4]
    letters = set(s[1:4].lower())
    palindromes = set()
    for word_length in range(3, len(mid) + 1):
        for perm in permutations(letters, word_length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes