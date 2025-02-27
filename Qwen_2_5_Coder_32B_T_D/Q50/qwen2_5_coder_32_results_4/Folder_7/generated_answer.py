from collections import defaultdict

def if_contains_anagrams(words):
    count_map = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            count_map[w] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count_map.values()))
    return anagram_pairs >= 178