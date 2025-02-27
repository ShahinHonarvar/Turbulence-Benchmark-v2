from collections import Counter

def if_contains_anagrams(strings):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = Counter()
    for s in strings:
        if len(s) >= 3:
            normalized = normalize_string(s)
            anagram_count[normalized] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs >= 97