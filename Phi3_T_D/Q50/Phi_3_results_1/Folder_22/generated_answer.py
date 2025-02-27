from collections import defaultdict

def if_contains_anagrams(strings):
    counts_map = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            counts_map[sorted_str] += 1
    pairs = sum((count * (count - 1) // 2 for count in counts_map.values() if count > 1))
    return pairs >= 72