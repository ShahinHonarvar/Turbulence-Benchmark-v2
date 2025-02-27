from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(int)
    for item in lst:
        if len(item) >= 3:
            sorted_item = ''.join(sorted(item.lower()))
            anagram_dict[sorted_item] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs >= 52