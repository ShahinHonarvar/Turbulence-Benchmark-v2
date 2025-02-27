from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    start, end = (4, 5)
    substring = s[start:end + 1]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes