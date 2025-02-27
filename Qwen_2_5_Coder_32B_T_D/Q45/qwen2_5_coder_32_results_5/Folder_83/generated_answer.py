from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:10])).lower()
    count = Counter(letters)
    half = []
    middle = ''
    for char, cnt in count.items():
        half += char * (cnt // 2)
        if cnt % 2 and (not middle):
            middle = char
    result = set()
    for p in permutations(half):
        palindrome = ''.join(p) + middle + ''.join(p)[::-1]
        if len(palindrome) >= 7:
            result.add(palindrome)
    return result