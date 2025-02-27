from collections import Counter

def if_contains_anagrams(lst):

    def count_anagrams(strings):
        counts = Counter()
        for s in strings:
            s = s.lower()
            if len(s) >= 3:
                sorted_s = ''.join(sorted(s))
                counts[sorted_s] += 1
        return counts
    anagram_counts = count_anagrams(lst)
    pairs = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pairs >= 65