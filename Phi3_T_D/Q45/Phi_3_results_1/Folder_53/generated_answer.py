from itertools import permutations

def palindromes_between_indices(s):
    letters = [letter.lower() for letter in s[4:9]]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes