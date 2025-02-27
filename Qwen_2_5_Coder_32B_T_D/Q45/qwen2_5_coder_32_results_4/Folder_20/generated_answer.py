from collections import Counter
    import itertools

def palindromes_between_indices(s):
    s = s[2:9].lower()
    letters = [char for char in s if char.isalpha()]
    count = Counter(letters)
    mid, even_half = ('', [])
    for char, cnt in count.items():
        if cnt % 2 == 1 and mid == '':
            mid = char
        even_half.extend(char * (cnt // 2))
    palindromes = set()
    for half in set(itertools.permutations(even_half)):
        half_str = ''.join(half)
        palindromes.add(half_str + mid + half_str[::-1])
    return {p for p in palindromes if len(p) >= 4}