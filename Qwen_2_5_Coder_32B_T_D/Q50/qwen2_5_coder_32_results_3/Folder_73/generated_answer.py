from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = Counter()
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            anagram_count[''.join(sorted(s))] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pairs >= 91