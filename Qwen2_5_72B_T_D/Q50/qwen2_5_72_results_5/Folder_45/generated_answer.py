from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagram_counts[normalize(word)] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs >= 277