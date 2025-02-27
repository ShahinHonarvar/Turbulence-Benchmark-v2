from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    substring = s[3:9]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            if is_palindrome(''.join(perm)):
                palindromes.add(''.join(perm))
    return palindromes