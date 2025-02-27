from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
    return anagram_pairs >= 60

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) >= 3 and len(s2) >= 3:
        return Counter(s1) == Counter(s2)
    else:
        return False