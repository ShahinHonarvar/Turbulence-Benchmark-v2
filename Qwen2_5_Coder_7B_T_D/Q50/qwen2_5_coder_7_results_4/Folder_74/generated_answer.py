from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    anagram_pairs = sum((len(value) * (len(value) - 1) // 2 for value in anagrams.values()))
    return anagram_pairs >= 17