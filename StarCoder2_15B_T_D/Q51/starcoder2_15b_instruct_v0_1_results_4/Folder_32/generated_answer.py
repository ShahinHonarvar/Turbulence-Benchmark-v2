from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 89:
                    return False
    return True

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    if Counter(s1) == Counter(s2):
        return True
    return False