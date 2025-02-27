from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    sorted_lst = [''.join(sorted(word)) for word in lst]
    counter = Counter(sorted_lst)
    anagram_pairs = sum((v * (v - 1) // 2 for v in counter.values()))
    return anagram_pairs >= 95