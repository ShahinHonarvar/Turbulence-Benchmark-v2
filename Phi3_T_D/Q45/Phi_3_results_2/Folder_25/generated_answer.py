from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    substring = s[1:5].lower()
    letter_counts = {}
    for letter in substring:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    palindromes = set()
    for length in range(3, sum(letter_counts.values()) + 1):
        for items in permutations(sorted(letter_counts.keys()), length):
            if is_palindrome(''.join(sorted(items))) and len(set(items)) * max(letter_counts.values()) >= length:
                palindromes.add(''.join(items).capitalize())
    return palindromes