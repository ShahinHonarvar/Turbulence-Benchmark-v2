import collections

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1 = strings[i].lower()
            s2 = strings[j].lower()
            if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2)):
                anagram_pairs += 1
                if anagram_pairs > 392:
                    return False
    return anagram_pairs <= 392