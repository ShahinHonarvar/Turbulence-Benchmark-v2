from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_count = 0
    anagrams_map = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            normalized = ''.join(sorted(string.lower()))
            anagrams_map[normalized] += 1
            anagrams_count += anagrams_map[normalized]
    return anagrams_count - len(strings) <= 54