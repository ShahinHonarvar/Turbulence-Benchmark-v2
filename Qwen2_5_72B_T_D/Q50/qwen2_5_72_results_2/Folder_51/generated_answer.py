from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            d[''.join(sorted(word.lower()))] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in d.values()))
    return anagram_pairs >= 39