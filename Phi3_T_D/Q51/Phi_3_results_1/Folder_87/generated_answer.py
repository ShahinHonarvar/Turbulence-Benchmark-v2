from collections import defaultdict

def if_contains_anagrams(strings):
    count_map = defaultdict(int)
    for s in strings:
        cleaned = ''.join((e for e in s.lower() if e.isalpha()))
        sorted_s = ''.join(sorted(cleaned))
        count_map[sorted_s] += 1
    pairs = sum((n * (n - 1) // 2 for n in count_map.values() if n > 1))
    return pairs <= 392