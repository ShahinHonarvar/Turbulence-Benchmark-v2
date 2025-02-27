from collections import defaultdict
from itertools import permutations

def get_sorted_tuples(lst):
    temp_lst = [''.join(sorted(word.lower())) for word in lst]
    return zip(lst, temp_lst)

def if_contains_anagrams(words):
    sorted_tuples = get_sorted_tuples(words)
    frequency_of_letters = defaultdict(int)
    for _, sorted_word in sorted_tuples:
        if len(sorted_word) >= 3:
            for p in permutations(sorted_word):
                anagram = ''.join(p)
                frequency_of_letters[anagram] += 1
    count_of_anagrams = sum((1 for freq in frequency_of_letters.values() if freq >= 2))
    return count_of_anagrams >= 276