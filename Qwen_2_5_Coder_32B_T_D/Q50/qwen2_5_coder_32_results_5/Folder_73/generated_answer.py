from collections import Counter
    from itertools import combinations

def if_contains_anagrams(words):
    count_dict = Counter((''.join(sorted(w.lower())) for w in words if len(w) >= 3))
    anagram_pairs = sum((v * (v - 1) // 2 for v in count_dict.values()))
    return anagram_pairs >= 91