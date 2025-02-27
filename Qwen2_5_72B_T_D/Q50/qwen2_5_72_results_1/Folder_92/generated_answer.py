from collections import Counter

def if_contains_anagrams(lst):
    lower_lst = [word.lower() for word in lst]
    sorted_lst = [''.join(sorted(word)) for word in lower_lst if len(word) >= 3]
    count = Counter(sorted_lst)
    pairs = sum((freq >= 2 for freq in count.values()))
    return pairs >= 2