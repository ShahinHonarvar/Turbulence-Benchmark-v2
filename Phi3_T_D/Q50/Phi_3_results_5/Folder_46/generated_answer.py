from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    length_filtered = [s for s in strings if len(s) >= 3]
    anagram_count = defaultdict(int)
    for s in length_filtered:
        sorted_str = ''.join(sorted(s.lower()))
        anagram_count[sorted_str] += 1
    count_pairs = sum((c // 2 for c in anagram_count.values()))
    return count_pairs >= 38