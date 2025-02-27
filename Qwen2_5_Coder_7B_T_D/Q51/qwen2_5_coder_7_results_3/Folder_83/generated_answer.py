from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = sorted(lst[i].lower())
            s2 = sorted(lst[j].lower())
            if s1 == s2 and len(s1) >= 3:
                anagram_count += 1
                if anagram_count > 19:
                    return False
    return True