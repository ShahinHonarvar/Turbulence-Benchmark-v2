from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_dict[''.join(sorted(word.lower()))].append(word)
    anagram_pairs = sum((len(list(combinations(words, 2))) for words in anagram_dict.values() if len(words) > 1))
    return anagram_pairs <= 79