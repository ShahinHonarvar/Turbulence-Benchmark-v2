from collections import Counter

def if_contains_anagrams(lst):
    normalized_lst = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    anagram_counts = Counter(normalized_lst)
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 464