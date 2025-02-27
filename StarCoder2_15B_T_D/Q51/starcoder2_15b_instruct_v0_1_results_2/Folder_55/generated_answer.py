import re

def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 44:
                    return False
    return True

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = re.sub('[^a-z]+', '', s1)
    s2 = re.sub('[^a-z]+', '', s2)
    if len(s1) != len(s2):
        return False
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    return s1_sorted == s2_sorted