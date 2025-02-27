from collections import Counter

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = Counter([sort_string(s) for s in strings if len(s) >= 3])
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 147