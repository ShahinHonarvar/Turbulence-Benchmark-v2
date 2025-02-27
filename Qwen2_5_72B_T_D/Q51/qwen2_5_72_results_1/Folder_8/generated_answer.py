from collections import Counter

def if_contains_anagrams(lst):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = Counter()
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            canonical = canonical_form(word)
            anagram_counts[canonical] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 68