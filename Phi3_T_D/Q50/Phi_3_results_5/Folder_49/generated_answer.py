from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    pairs = 0
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            anagrams[sorted_str].append(string)
    for _, group in anagrams.items():
        if len(group) >= 2:
            pairs += len(group) // 2
    return pairs >= 59