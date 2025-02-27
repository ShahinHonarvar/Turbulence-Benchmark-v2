from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(text):
    text_slice = text[2:10]
    letters = ''.join(filter(str.isalpha, text_slice)).lower()
    length = 7
    palindromes = set()
    for perm in set(permutations(letters, length)):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes