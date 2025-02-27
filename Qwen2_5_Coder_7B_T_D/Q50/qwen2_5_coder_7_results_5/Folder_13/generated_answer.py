from collections import Counter

def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string] = anagram_dict.get(sorted_string, 0) + 1
    count = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return count >= 144