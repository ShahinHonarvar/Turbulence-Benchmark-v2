import re
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagrams += 1
                if anagrams > 86:
                    return False
    return True

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = re.sub('[^a-z]+', '', s1)
    s2 = re.sub('[^a-z]+', '', s2)
    if len(s1) >= 3 and len(s2) >= 3:
        return Counter(s1) == Counter(s2)
    return False