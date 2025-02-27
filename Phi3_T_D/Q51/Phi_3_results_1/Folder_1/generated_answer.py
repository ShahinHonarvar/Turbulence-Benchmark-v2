import collections

def if_contains_anagrams(strings):
    anagram_counts = collections.defaultdict(int)
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s.lower()))
            anagram_counts[sorted_str] += 1
    return sum((1 for count in anagram_counts.values() if count > 1)) <= 30