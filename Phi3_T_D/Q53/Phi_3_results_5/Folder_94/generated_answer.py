import re
    from itertools import combinations

def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters_only = re.sub('[^a-z]', '', s.lower())
    palindromes = set()
    for length in range(41, len(letters_only) + 1):
        for combo in combinations(letters_only, length):
            word = ''.join(combo)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes