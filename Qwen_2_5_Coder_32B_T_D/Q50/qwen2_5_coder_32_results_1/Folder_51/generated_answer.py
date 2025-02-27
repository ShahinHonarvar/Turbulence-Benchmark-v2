from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for string in strings:
        s = ''.join(sorted(string.lower()))
        if len(s) >= 3:
            anagram_count[s] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs >= 39