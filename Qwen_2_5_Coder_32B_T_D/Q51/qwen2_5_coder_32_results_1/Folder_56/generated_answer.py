from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            anagram_map[w].append(word)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_map.values()))
    return anagram_count <= 11