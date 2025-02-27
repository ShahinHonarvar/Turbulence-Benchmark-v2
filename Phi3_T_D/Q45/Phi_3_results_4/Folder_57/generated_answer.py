from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    characters = [s[i].lower() for i in range(2, 6) if s[i].isalpha()]
    palindromes = set()
    for perm in permutations(characters, 5):
        candidate = ''.join(perm)
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes