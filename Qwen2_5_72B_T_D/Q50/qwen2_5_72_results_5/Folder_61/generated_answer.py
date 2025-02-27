from collections import Counter

def if_contains_anagrams(strings):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_counter = Counter()
    for s in strings:
        if len(s) >= 3:
            normalized = normalize_string(s)
            anagram_counter[normalized] += 1
    anagram_pairs = sum((count // 2 for count in anagram_counter.values()))
    return anagram_pairs >= 8