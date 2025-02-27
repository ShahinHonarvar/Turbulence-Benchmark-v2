from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:7])).lower()
    count = Counter(letters)
    if len(letters) < 6:
        return set()
    mid = ''
    sides = ''
    for char, cnt in count.items():
        if cnt % 2:
            if mid:
                return set()
            mid = char
        sides += char * (cnt // 2)
    palindromes = set()
    for side in set(permutations(sides, len(sides))):
        palindrome = ''.join(side) + mid + ''.join(side[::-1])
        palindromes.add(palindrome)
    return palindromes