from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagrams = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagrams[sorted_s].append(s_lower)
    for group in anagrams.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
            if count > 173:
                return False
    return True