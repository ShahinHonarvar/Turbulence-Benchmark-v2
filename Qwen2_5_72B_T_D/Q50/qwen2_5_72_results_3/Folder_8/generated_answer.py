from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            anagram_counts[''.join(sorted(s.lower()))] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) >= 85