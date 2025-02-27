from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if s and s.isalpha()]
    anagram_pairs = 0
    for i in range(len(strings)):
        if len(strings[i]) >= 3:
            for j in range(i + 1, len(strings)):
                if Counter(strings[i]) == Counter(strings[j]):
                    anagram_pairs += 1
    return anagram_pairs <= 44