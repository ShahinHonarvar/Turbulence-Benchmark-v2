from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i, s1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            s2 = strings[j]
            if len(s1) >= 3 and len(s2) >= 3 and (Counter(s1.lower()) == Counter(s2.lower())):
                anagram_pairs += 1
                if anagram_pairs >= 52:
                    return True
    return False