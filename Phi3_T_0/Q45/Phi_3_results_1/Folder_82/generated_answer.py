from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = s[1:7].lower()
    unique_letters = ''.join(set(letters))
    palindromes = set()
    for length in range(7, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes