from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = 0
    temp_dict = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        temp_dict[sorted_string].append(string)
    for word_list in temp_dict.values():
        if len(word_list) > 1:
            for word1, word2 in combinations(word_list, 2):
                if len(word1) >= 3 and len(word2) >= 3:
                    anagram_count += 1
    return anagram_count >= 70