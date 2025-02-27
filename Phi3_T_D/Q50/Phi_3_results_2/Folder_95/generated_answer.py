from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_chars = ''.join(sorted(string.lower()))
            sorted_anagrams[sorted_chars].append(string)
    pairs = 0
    for anagrams in sorted_anagrams.values():
        pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return pairs >= 93