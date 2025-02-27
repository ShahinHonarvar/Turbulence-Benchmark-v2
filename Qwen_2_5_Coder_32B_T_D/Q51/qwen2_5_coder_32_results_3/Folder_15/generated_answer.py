from collections import Counter
    from itertools import combinations

def if_contains_anagrams(words):
    word_counts = Counter((''.join(sorted(w.lower())) for w in words if len(w) >= 3))
    anagram_pairs = sum((count * (count - 1) // 2 for count in word_counts.values()))
    return anagram_pairs <= 20