from collections import Counter

def if_contains_anagrams(lst):
    normalized_lst = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    count = Counter(normalized_lst)
    anagram_pairs = sum((val * (val - 1) // 2 for val in count.values()))
    return anagram_pairs >= 55