from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counter = Counter()
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            anagram_counter[normalized] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counter.values()))
    return anagram_pairs >= 55