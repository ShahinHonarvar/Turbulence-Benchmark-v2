import re
from collections import Counter

def if_contains_anagrams(lst):
    """
    Returns True if there are at most 85 pairs of anagrams in the given list; otherwise, returns False.
    Anagrams are defined as strings that contain the same letters, ignoring case and excluding punctuation.
    Anagrams must be of length at least three.
    """
    anagram_pairs = 0
    pattern = re.compile('[^a-zA-Z]+')
    for i, word1 in enumerate(lst):
        for word2 in lst[i + 1:]:
            word1_clean = pattern.sub('', word1).lower()
            word2_clean = pattern.sub('', word2).lower()
            if len(word1_clean) >= 3 and len(word2_clean) >= 3 and (Counter(word1_clean) == Counter(word2_clean)):
                anagram_pairs += 1
                if anagram_pairs > 85:
                    return False
    return anagram_pairs <= 85