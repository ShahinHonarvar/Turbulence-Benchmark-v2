from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                anagram_pairs += 1
    return anagram_pairs <= 34

def are_anagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) < 3 or len(s2) < 3:
        return False
    return Counter(s1) == Counter(s2)