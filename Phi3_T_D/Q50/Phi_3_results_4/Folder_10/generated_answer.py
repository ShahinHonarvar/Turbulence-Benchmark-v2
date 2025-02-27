from collections import defaultdict
import itertools

def char_count_key(word):
    return tuple(sorted(word.lower()))

def if_contains_anagrams(word_list):
    filtered = [word for word in word_list if len(word) >= 3]
    count_dict = defaultdict(int)
    for word in filtered:
        count_dict[char_count_key(word)] += 1
    return sum((count > 1 for count in count_dict.values())) >= 52