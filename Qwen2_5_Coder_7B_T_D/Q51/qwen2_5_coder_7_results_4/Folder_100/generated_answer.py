from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_map.values() if len(v) > 1))
    return anagram_pairs <= 98