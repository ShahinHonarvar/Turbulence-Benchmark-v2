from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = ''.join([c for c in s if c.isalpha()])
    counter = Counter(letters)
    mid = ''
    sides = []
    for letter, count in counter.items():
        if count % 2 == 1 and (not mid):
            mid = letter
        sides.extend(letter * (count // 2))
    palindromes = set()
    for perm in set(permutations(sides)):
        palindrome = ''.join(perm) + mid + ''.join(reversed(perm))
        if len(palindrome) >= 5:
            palindromes.add(palindrome)
    return palindromes