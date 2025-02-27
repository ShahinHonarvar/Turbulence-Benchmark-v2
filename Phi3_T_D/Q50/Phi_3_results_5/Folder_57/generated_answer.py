from collections import defaultdict

def if_contains_anagrams(strings):
    count_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            count_map[key] += 1
    return sum((x >= 2 for x in count_map.values())) >= 50