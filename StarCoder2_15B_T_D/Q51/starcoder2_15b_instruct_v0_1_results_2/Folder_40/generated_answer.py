from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = Counter()
    for s in strings:
        s = s.lower()
        if len(s) >= 3 and all((c.isalpha() for c in s)):
            s_sorted = ''.join(sorted(s))
            anagram_counts[s_sorted] += 1
    return max(anagram_counts.values()) <= 29