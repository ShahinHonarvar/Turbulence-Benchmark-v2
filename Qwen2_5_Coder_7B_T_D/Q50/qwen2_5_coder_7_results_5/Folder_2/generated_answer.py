from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            counter = Counter(sorted_s)
            anagram_count += sum((v * (v - 1) // 2 for v in counter.values()))
    return anagram_count >= 246