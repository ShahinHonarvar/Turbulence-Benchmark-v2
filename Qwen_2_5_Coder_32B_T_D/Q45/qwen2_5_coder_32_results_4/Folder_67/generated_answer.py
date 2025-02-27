from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:7])).lower()
    counts = Counter(letters)
    if len(letters) < 5:
        return set()
    half = ''
    middle = ''
    for letter, count in counts.items():
        half += letter * (count // 2)
        if count % 2 and (not middle):
            middle = letter
    if len(half) < 2:
        return set()
    palindromes = set()
    for p in permutations(half):
        palindrome = ''.join(p) + middle + ''.join(reversed(p))
        palindromes.add(palindrome)
    return palindromes