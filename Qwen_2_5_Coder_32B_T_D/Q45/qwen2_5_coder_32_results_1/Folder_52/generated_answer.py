from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:8])).lower()
    count = Counter(letters)
    mid, halves = ('', [])
    for char, freq in count.items():
        mid += char * (freq % 2)
        halves.append(char * (freq // 2))
    if len(mid) > 1:
        return set()
    palindromes = set()
    for half in itertools.permutations(''.join(halves)):
        half_str = ''.join(half)
        palindromes.add(half_str + mid + half_str[::-1])
    return {p for p in palindromes if len(p) >= 6}