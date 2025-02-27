from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3 and word.isalpha()]
    anagram_dict = {}
    for word in lst:
        key = tuple(sorted(Counter(word).items()))
        anagram_dict[key] = anagram_dict.get(key, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pairs <= 60