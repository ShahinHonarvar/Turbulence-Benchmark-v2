from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_pairs = 0
    anagram_map = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_map[sorted_string].append(string)
    for anagrams in anagram_map.values():
        anagram_pairs += len(anagrams) // 2
    return anagram_pairs >= 36