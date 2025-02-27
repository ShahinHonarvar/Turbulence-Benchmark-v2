from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[1:8] if c.isalpha()])
    counter = Counter(letters)
    usable_letters = ''.join([c * (v // 2) for c, v in counter.items()])
    palindromes = set()
    for perm in permutations(usable_letters):
        half = ''.join(perm)
        middle = [c for c, v in counter.items() if v % 2][0] if any((v % 2 for v in counter.values())) else ''
        palindrome = half + middle + half[::-1]
        if len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes