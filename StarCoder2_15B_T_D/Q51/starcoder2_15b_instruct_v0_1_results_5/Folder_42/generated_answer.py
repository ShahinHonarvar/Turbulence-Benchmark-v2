import re

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 38:
                    return False
    return anagram_pairs <= 38

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = re.sub('[^a-z]', '', s1)
    s2 = re.sub('[^a-z]', '', s2)
    if len(s1) != len(s2):
        return False
    count = [0] * 26
    for c in s1:
        count[ord(c) - ord('a')] += 1
    for c in s2:
        count[ord(c) - ord('a')] -= 1
    for i in range(26):
        if count[i] != 0:
            return False
    return True