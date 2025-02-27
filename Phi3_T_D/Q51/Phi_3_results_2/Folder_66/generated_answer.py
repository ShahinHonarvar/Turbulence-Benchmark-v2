from itertools import combinations
from collections import Counter
import re

def clean_str(s):
    return re.sub('[^a-zA-Z]', '', s).lower()

def anagram_pairs(str_list):
    anagram_pairs_count = 0
    cleaned_strs = [clean_str(s) for s in str_list]
    for a, b in combinations(cleaned_strs, 2):
        if len(a) >= 3 and len(b) >= 3 and (Counter(a) == Counter(b)) and (a != b):
            anagram_pairs_count += 1
    return anagram_pairs_count

def if_contains_anagrams(str_list):
    return anagram_pairs(str_list) <= 64