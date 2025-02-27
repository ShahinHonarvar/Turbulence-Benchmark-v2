from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            anagrams[sorted_string] += 1
    anagram_pairs = 0
    for count in anagrams.values():
        anagram_pairs += count // 2
    return anagram_pairs <= 4