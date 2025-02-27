from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string].append(string)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_count <= 78