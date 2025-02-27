from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    letters = s[5:10]
    unique_letters = set(letters.lower())
    palindromes = set()
    for length in range(4, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes