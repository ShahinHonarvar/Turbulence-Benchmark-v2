from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s in strings:
        if len(s) >= 3:
            s = s.lower()
            sorted_s = ''.join(sorted(s))
            counts = Counter(sorted_s)
            pairs = 0
            for count in counts.values():
                pairs += count * (count - 1) // 2
            anagram_pairs += pairs
    return anagram_pairs >= 17