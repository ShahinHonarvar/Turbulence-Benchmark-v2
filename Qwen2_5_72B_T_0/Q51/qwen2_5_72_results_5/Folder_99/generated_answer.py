from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_counter = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if Counter(strings[i]) == Counter(strings[j]):
                anagram_counter += 1
    return anagram_counter <= 93