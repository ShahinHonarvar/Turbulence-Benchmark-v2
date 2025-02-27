from collections import defaultdict

def if_contains_anagrams(strings):
    string_count = defaultdict(int)
    anagram_pairs = 0
    for string in strings:
        normalized = ''.join(sorted(string.lower()))
        string_count[normalized] += 1
        if string_count[normalized] == 2:
            anagram_pairs += 1
    return anagram_pairs >= 74