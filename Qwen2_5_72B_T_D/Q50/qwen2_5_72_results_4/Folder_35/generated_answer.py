from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    anagram_dict = Counter([''.join(sorted(word)) for word in lst])
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pairs_count >= 153