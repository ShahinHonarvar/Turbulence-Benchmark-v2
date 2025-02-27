from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_tuple(word):
        return tuple(sorted(word.lower()))
    anagram_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagram_dict[sorted_tuple(word)] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs >= 64