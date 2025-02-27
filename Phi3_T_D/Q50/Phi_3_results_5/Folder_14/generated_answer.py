from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams_counter = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            anagrams_counter[normalized] += 1
    anagram_pairs = sum((count // 2 for count in anagrams_counter.values()))
    return anagram_pairs >= 22