from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:3] if c.lower() in string.ascii_lowercase]
    if len(letters) < 3:
        return set()
    letter_counts = Counter(letters)
    half_palindrome = []
    middle_char = ''
    for letter, count in letter_counts.items():
        half_palindrome.extend([letter] * (count // 2))
        if count % 2 and (not middle_char):
            middle_char = letter
    palindromes = set()
    for p in permutations(half_palindrome):
        half = ''.join(p)
        full_palindrome = half + middle_char + half[::-1]
        palindromes.add(full_palindrome)
    return palindromes