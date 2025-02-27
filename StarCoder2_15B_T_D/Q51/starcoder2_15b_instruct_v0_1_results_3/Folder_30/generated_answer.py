from collections import Counter

def if_contains_anagrams(strings):
    anagram_freq = Counter()
    for s in strings:
        if len(s) >= 3:
            anagram_freq.update([''.join(sorted(s.lower()))])
    return len([freq for freq in anagram_freq.values() if freq > 1]) <= 28