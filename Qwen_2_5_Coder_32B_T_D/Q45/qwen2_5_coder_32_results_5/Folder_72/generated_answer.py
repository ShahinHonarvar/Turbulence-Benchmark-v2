from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    letter_counts = Counter(letters)
    half_palindrome = []
    middle = ''
    for letter, count in letter_counts.items():
        half_palindrome.extend(letter * (count // 2))
        if count % 2 and (not middle):
            middle = letter
    half_palindrome_length = len(half_palindrome)
    palindromes = set()
    for combo in permutations(half_palindrome):
        palindrome = ''.join(combo) + middle + ''.join(reversed(combo))
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return {p for p in palindromes if len(p) >= 6}