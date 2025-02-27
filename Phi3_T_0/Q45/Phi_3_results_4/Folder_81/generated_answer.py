from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[0:7].lower()
    letters = ''.join(filter(str.isalpha, s))
    unique_letters = set(letters)
    palindromes = set()
    for length in range(3, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes