from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for string in strings:
        s = ''.join(sorted(string.lower()))
        if len(s) >= 3:
            anagram_counts[s] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) >= 20