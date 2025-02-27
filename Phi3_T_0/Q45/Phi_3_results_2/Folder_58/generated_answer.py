from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    letters = [char.lower() for char in s[:7] if char.isalpha()]
    unique_letters = set(letters)
    palindromes = set()
    for length in range(6, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes