from collections import defaultdict
import itertools

def if_contains_anagrams(lst):

    def count_anagrams(words):
        anagram_groups = defaultdict(list)
        for word in words:
            sorted_word = tuple(sorted(word.lower()))
            anagram_groups[sorted_word].append(word)
        return sum((1 for group in anagram_groups.values() if len(group) > 1 and len(group[0]) >= 3))
    all_combinations = list(itertools.combinations(lst, 2))
    return count_anagrams(lst) <= 113 * len(all_combinations)