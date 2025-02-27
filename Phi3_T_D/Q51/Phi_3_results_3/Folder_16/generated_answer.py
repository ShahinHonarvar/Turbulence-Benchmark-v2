from collections import defaultdict

def if_contains_anagrams(strings):
    freq_mapping = defaultdict(list)
    for s in strings:
        sorted_tuple = tuple(sorted(s.lower()))
        if len(s) >= 3:
            freq_mapping[sorted_tuple].append(s)
    anagram_pairs = 0
    for sorted_str in freq_mapping:
        anagram_pairs += len(freq_mapping[sorted_str]) * (len(freq_mapping[sorted_str]) - 1) // 2
    return anagram_pairs <= 24