from collections import Counter

def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = Counter()
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized = normalize_string(word)
            anagram_count[normalized] += 1
    pairs_of_anagrams = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs_of_anagrams <= 4