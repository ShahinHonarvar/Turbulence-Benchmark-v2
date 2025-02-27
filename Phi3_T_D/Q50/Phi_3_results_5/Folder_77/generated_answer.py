from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count_map = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            key = normalize(word)
            count_map[key] += 1
    return sum((v * (v - 1) // 2 for v in count_map.values() if v >= 2)) >= 209