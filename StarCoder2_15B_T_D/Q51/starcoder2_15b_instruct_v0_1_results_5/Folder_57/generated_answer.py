import re

def if_contains_anagrams(strings):
    anagram_threshold = 74
    letters = set('abcdefghijklmnopqrstuvwxyz')
    min_length = 3

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return len(s1) >= min_length and len(s2) >= min_length and (set(s1) == set(s2)) and all((s1.count(ch) == s2.count(ch) for ch in letters))
    anagram_count = 0
    for i, s1 in enumerate(strings):
        for s2 in strings[i + 1:]:
            if is_anagram(s1, s2):
                anagram_count += 1
                if anagram_count > anagram_threshold:
                    return False
    return True