import itertools
from collections import defaultdict

def count_anagrams(words):

    def to_key(word):
        return ''.join(sorted(word.lower()))
    anagrams_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagrams_map[to_key(word)].append(word)
    pairs = 0
    for word_list in anagrams_map.values():
        if len(word_list) > 1:
            pairs += itertools.combinations(word_list, 2).__len__()
    return pairs <= 279

def if_contains_anagrams(strings_list):
    return count_anagrams(strings_list)