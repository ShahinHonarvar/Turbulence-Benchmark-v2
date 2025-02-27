from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_map = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_map[sorted_word].append(word)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_map.values() if len(v) > 1))
    return anagram_pairs >= 44