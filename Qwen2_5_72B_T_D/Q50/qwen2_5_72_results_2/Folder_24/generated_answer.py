from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s))
        anagram_dict[sorted_s] = anagram_dict.get(sorted_s, 0) + 1
    anagram_counts = [count for count in anagram_dict.values() if count > 1]
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts))
    return anagram_pairs >= 65