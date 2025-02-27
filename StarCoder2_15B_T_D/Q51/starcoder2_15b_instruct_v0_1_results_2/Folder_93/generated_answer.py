import re

def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 36:
                    return False
    return True

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = re.sub('[^a-z]+', '', s1)
    s2 = re.sub('[^a-z]+', '', s2)
    if len(s1) >= 3 and len(s2) >= 3:
        return sorted(s1) == sorted(s2)
    else:
        return False