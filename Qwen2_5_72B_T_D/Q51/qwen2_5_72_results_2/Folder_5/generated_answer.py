from collections import Counter

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = Counter()
    for item in lst:
        if len(item) >= 3 and item.isalpha():
            norm_item = normalize(item)
            anagram_counts[norm_item] += 1
    anagram_pairs = sum((count >= 2 for count in anagram_counts.values()))
    return anagram_pairs <= 4