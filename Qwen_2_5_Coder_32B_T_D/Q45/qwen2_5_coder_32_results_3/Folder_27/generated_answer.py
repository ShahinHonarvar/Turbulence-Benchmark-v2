from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c in string.ascii_letters]
    letter_counts = Counter(letters)
    half_len = 3
    half_palindrome = []
    for letter, count in letter_counts.items():
        half_palindrome.extend([letter] * (count // 2))
    if len(half_palindrome) < half_len:
        return set()
    palindromes = set()
    for half in permutations(half_palindrome, half_len):
        half = ''.join(half)
        full_palindrome = half + (half[-2::-1] if len(half_palindrome) % 2 == 0 else half[-1] + half[-2::-1])
        palindromes.add(full_palindrome)
    return palindromes