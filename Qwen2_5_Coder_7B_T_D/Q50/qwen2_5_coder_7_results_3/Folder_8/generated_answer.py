from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_map = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            anagram_map[''.join(sorted(word_lower))].append(word_lower)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_map.values() if len(v) >= 2))
    return anagram_pairs >= 85