from collections import Counter

def if_contains_anagrams(words):
    anagram_counts = Counter((''.join(sorted(w.lower())) for w in words if len(w) >= 3))
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 10