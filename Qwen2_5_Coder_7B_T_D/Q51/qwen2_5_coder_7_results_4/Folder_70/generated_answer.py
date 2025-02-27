from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    strings = [s.lower() for s in strings if len(s) >= 3]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if Counter(strings[i]) == Counter(strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 97:
                    return False
    return True