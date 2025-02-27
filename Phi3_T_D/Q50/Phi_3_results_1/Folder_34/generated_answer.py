from collections import defaultdict
import itertools

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    anagram_pairs = 0
    for word_list in anagrams.values():
        if len(word_list) > 1:
            combinations = list(itertools.combinations(word_list, 2))
            anagram_pairs += len(combinations)
    return anagram_pairs >= 25