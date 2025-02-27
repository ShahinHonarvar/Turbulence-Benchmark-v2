from collections import Counter

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = Counter()
    for word in lst:
        if len(word) >= 3:
            anagram_counts[normalize(word)] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 219