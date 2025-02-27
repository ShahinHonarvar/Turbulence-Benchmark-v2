from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_counter = 0
    for i in range(len(strings)):
        if len(strings[i]) >= 3:
            for j in range(i + 1, len(strings)):
                if len(strings[j]) >= 3:
                    if Counter(strings[i]) == Counter(strings[j]):
                        anagram_counter += 1
    return anagram_counter <= 49