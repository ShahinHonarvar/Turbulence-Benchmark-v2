from collections import Counter, defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagrams = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] += 1
            count += anagrams[sorted_s] - 1
    return count <= 279