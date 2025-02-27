from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    counts = Counter((''.join(sorted(word)) for word in lst))
    anagram_pairs = sum((cnt * (cnt - 1) // 2 for cnt in counts.values()))
    return anagram_pairs >= 54