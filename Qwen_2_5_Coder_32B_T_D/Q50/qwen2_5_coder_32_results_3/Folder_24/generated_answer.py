from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagrams = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagrams[sorted_s].append(s_lower)
    for lst in anagrams.values():
        n = len(lst)
        if n > 1:
            count += n * (n - 1) // 2
    return count >= 65