from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    pairs_count = 0
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            anagram_map[key].append(s)
    for _, v in anagram_map.items():
        n = len(v)
        while n > 1:
            n -= 2
            pairs_count += n
            if pairs_count > 89:
                return False
    return True