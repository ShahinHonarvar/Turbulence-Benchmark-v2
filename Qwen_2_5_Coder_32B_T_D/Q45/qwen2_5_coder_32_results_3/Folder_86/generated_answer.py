from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[6:10])).lower()
    count = Counter(letters)
    half = []
    middle = ''
    for char in count:
        if count[char] // 2 > 0:
            half.extend(char * (count[char] // 2))
        if count[char] % 2 == 1 and (not middle):
            middle = char
    palindromes = set()
    for perm in permutations(half):
        half_str = ''.join(perm)
        palindromes.add(half_str + middle + half_str[::-1])
    return {p for p in palindromes if len(p) >= 4}