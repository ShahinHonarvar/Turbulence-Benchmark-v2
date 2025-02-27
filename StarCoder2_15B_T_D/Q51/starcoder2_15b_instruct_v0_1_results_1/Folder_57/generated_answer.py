from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    pairs = 0
    for anagram_list in anagrams.values():
        pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return pairs <= 74