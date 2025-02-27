from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    s = s[1:10].lower()
    letters = [c for c in s if c in string.ascii_lowercase]
    letter_counts = Counter(letters)
    half_len = 3
    mid_char = ''
    half = []
    for letter, count in letter_counts.items():
        half.extend(letter * (count // 2))
        if count % 2 and (not mid_char):
            mid_char = letter
    palindromes = set()
    for p in permutations(half, half_len):
        p = ''.join(p)
        palindromes.add(p + mid_char + p[::-1])
    return palindromes