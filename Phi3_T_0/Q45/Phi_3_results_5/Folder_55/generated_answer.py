from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    letters = [c.lower() for c in s[:3]]
    unique_letters = set(letters)
    palindromes = set()
    for perm in permutations(unique_letters):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes