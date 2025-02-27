from collections import Counter

def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        s = ''.join(filter(str.isalpha, s.lower()))
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            anagram_dict[sorted_str] = anagram_dict.get(sorted_str, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs <= 92