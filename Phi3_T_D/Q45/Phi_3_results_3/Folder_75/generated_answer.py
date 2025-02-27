from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    length = min(4 - 2 + 1 + 1, len(s) - 2)
    substring = s[2:length + 2]
    letter_counts = {}
    for letter in substring:
        letter_counts[letter.lower()] = letter_counts.get(letter.lower(), 0) + 1
    palindromes = set()
    for p in permutations(letter_counts):
        palindrome_candidate = ''.join((p * letter_counts[l] for l in letter_counts)).replace(' ', '')
        if is_palindrome(palindrome_candidate) and len(palindrome_candidate) >= 3:
            palindromes.add(palindrome_candidate)
    return palindromes