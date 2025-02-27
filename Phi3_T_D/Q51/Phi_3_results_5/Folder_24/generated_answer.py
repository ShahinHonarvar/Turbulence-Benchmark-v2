from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_map[sorted_str].append(s)
    count = 0
    for value in anagram_map.values():
        if len(value) > 1:
            pairs = len(value) * (len(value) - 1) // 2
            count += pairs
            if count > 96:
                return False
    return True