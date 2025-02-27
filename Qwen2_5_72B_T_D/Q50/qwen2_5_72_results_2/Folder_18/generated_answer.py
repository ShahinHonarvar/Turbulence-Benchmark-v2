from collections import Counter

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    sorted_lst = [''.join(sorted(word)) for word in lst]
    count = Counter(sorted_lst)
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs >= 106