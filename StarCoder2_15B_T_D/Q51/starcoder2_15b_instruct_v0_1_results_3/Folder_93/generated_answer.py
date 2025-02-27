from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 36:
                    return False
    return True

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) >= 3 and len(s2) >= 3:
        counter1 = Counter((c for c in s1 if c.isalpha()))
        counter2 = Counter((c for c in s2 if c.isalpha()))
        return counter1 == counter2
    else:
        return False