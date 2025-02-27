from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    selected_chars = s[1:8].lower()
    unique_chars = ''.join(set(selected_chars))
    palindrome_set = set()
    for length in range(7, len(selected_chars) + 1):
        for perm in permutations(unique_chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindrome_set.add(word)
    return palindrome_set