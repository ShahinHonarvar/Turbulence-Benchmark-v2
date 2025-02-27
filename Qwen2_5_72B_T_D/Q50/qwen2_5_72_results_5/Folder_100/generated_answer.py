from collections import Counter

def if_contains_anagrams(lst):
    lower_lst = [word.lower() for word in lst if len(word) >= 3]
    sorted_lst = [''.join(sorted(word)) for word in lower_lst]
    count = Counter(sorted_lst)
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs >= 95