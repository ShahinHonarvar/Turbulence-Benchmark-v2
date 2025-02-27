from collections import defaultdict
import itertools

def if_contains_anagrams(string_list):
    anagram_count = 0
    letter_set = set('abcdefghijklmnopqrstuvwxyz')

    def validate_word(word):
        return set(word.lower()) <= letter_set and len(word) >= 3
    anagram_dict = defaultdict(list)
    for word in filter(validate_word, string_list):
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    pairs = 0
    for word_list in anagram_dict.values():
        if len(word_list) > 1:
            pairs += sum((1 for _ in itertools.combinations(word_list, 2)))
        if pairs > 58:
            return False
    return True