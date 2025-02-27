from collections import Counter

def if_contains_anagrams(lst):
    lst = [item.lower() for item in lst if len(item) >= 3]
    sorted_lst = [''.join(sorted(item)) for item in lst]
    counter = Counter(sorted_lst)
    anagram_pairs = sum((count * (count - 1) // 2 for count in counter.values()))
    return anagram_pairs >= 7