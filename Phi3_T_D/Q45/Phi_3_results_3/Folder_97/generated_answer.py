import itertools

def is_palindrome(word):
    return word == word[::-1]

def palindromes_between_indices(s):
    substring = s[:5]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for letters_perm in itertools.permutations(letters, length):
            candidate = ''.join(letters_perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes