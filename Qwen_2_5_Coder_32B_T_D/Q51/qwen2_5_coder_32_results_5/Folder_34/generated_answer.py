from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagrams = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            arr = list(s)
            arr.sort()
            key = ''.join(arr)
            anagrams[key] += 1
    for n in anagrams.values():
        count += n * (n - 1) // 2
    return count <= 401