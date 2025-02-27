from collections import Counter

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = Counter()
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_counts[normalized_word] += 1
    anagram_pairs_count = sum((count - 1 for count in anagram_counts.values()))
    return anagram_pairs_count <= 21