from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:8])).lower()
    letter_counts = Counter(letters)
    half_len = 3

    def can_form_palindrome(counter):
        odd_count = sum((1 for count in counter.values() if count % 2 != 0))
        return odd_count <= 1
    if not can_form_palindrome(letter_counts):
        return set()
    half_palindrome_chars = []
    middle_char = ''
    for letter, count in letter_counts.items():
        half_palindrome_chars.extend(letter * (count // 2))
        if count % 2 != 0:
            middle_char = letter
    palindromes = set()
    for perm in permutations(half_palindrome_chars, half_len):
        half = ''.join(perm)
        palindrome = half + middle_char + half[::-1]
        palindromes.add(palindrome)
    return palindromes