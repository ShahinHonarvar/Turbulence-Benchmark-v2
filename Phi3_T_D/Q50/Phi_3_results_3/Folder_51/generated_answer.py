from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_map[sorted_s].append(s)
    count = 0
    for k in anagram_map:
        count += sum((1 for _ in range(len(anagram_map[k]) - 1)))
    return count >= 39