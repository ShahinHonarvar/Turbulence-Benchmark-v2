from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = [c for c in s if c in string.ascii_lowercase]
    letter_count = Counter(letters)
    palindromes = set()
    if len(letters) >= 7:
        for p in permutations(letters, 7):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes