from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = ''.join(filter(lambda x: x in string.ascii_letters, s[1:8])).lower()
    count = Counter(letters)
    mid, double = ('', '')
    for char, freq in count.items():
        mid += char * (freq % 2)
        double += char * (freq // 2)
    if len(mid) > 1:
        return set()
    palindromes = set()
    for perm in permutations(double):
        half = ''.join(perm)
        palindromes.add(half + mid + half[::-1])
    return palindromes