from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = ''.join(filter(lambda x: x in string.ascii_letters, s[3:10])).lower()
    n = len(letters)
    palindrome_set = set()
    if n < 7:
        return palindrome_set
    counts = Counter(letters)
    mid = ''
    sides = []
    odd_count = 0
    for char, cnt in counts.items():
        if cnt % 2 != 0:
            odd_count += 1
            mid = char
        sides.extend(char * (cnt // 2))
    if odd_count > 1:
        return palindrome_set
    for perm in permutations(sides, len(sides)):
        side_str = ''.join(perm)
        palindrome_set.add(side_str + mid + side_str[::-1])
    return {p for p in palindrome_set if len(p) >= 7}