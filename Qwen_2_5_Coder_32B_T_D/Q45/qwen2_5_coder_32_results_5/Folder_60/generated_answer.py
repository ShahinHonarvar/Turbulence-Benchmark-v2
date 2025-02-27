from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:7])).lower()
    if len(letters) < 4:
        return set()
    counter = Counter(letters)
    mid, sides = ('', '')
    for char, count in counter.items():
        if count % 2 == 1 and (not mid):
            mid = char
        sides += char * (count // 2)
    palindromes = set()
    for p in permutations(sides):
        palindrome = ''.join(p) + mid + ''.join(reversed(p))
        palindromes.add(palindrome)
    return palindromes