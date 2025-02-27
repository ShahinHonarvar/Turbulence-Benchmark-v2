from collections import Counter

def if_contains_anagrams(strings):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = Counter()
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            norm_str = normalize_string(s)
            anagrams[norm_str] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return anagram_pairs <= 366