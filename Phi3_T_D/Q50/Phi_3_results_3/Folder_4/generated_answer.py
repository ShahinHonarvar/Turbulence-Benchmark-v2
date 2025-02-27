from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_counts = defaultdict(int)
    for s in strings:
        key = tuple(sorted(s.lower()))
        anagram_counts[key] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values() if len(key) >= 3)) >= 42