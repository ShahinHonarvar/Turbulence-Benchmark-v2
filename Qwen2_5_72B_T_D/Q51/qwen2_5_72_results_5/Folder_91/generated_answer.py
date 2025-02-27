from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    filtered_strings = [s for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_dict = {}
    for s in filtered_strings:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    anagram_counts = [len(v) for v in anagram_dict.values() if len(v) > 1]
    total_anagram_pairs = sum((c * (c - 1) // 2 for c in anagram_counts))
    return total_anagram_pairs <= 88