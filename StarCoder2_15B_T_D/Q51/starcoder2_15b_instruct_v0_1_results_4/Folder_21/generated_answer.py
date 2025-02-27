import re
from collections import Counter

def if_contains_anagrams(strings):
    anagram_counter = Counter()
    for string in strings:
        string = re.sub('[^a-zA-Z]+', '', string).lower()
        if len(string) >= 3:
            anagram_key = ''.join(sorted(string))
            anagram_counter[anagram_key] += 1
    return max(anagram_counter.values()) <= 26