import itertools
    from collections import Counter

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:3])).lower()
    count = Counter(letters)
    mid, sides = ('', '')
    for char, cnt in count.items():
        if cnt % 2:
            if mid:
                return set()
            mid = char
        sides += char * (cnt // 2)
    palindromes = set()
    for p in set(itertools.permutations(sides)):
        palindrome = ''.join(p) + mid + ''.join(reversed(p))
        palindromes.add(palindrome)
    return palindromes if len(mid) + 2 * len(sides) >= 3 else set()