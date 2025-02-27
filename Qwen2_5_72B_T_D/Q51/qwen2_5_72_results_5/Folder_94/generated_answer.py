from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_pairs = 0
    for i, string in enumerate(strings):
        if len(string) >= 3:
            for j in range(i + 1, len(strings)):
                if len(strings[j]) == len(string):
                    if Counter(string) == Counter(strings[j]):
                        anagram_pairs += 1
    return anagram_pairs <= 181