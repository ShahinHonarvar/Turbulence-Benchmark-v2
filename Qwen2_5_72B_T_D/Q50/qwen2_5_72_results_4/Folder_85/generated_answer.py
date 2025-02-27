from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s] = anagram_dict.get(sorted_s, 0) + 1
    anagram_counts = Counter(anagram_dict.values())
    total_pairs = 0
    for count in anagram_counts:
        if count > 1:
            total_pairs += count * (count - 1) // 2
    return total_pairs >= 73