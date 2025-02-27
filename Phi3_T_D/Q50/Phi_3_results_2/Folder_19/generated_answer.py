from collections import defaultdict
import itertools

def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    possible_pairs = itertools.combinations(strings, 2)
    anagram_pairs = filter(lambda pair: are_anagrams(*pair), possible_pairs)
    anagram_count = sum((1 for _ in anagram_pairs if len(next(iter(pair))) >= 3))
    return anagram_count >= 84