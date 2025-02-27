import re

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i, first_string in enumerate(strings):
        for j in range(i + 1, len(strings)):
            second_string = strings[j]
            if sorted(first_string.lower()) == sorted(second_string.lower()) and len(first_string) >= 3 and (len(second_string) >= 3):
                anagram_pairs += 1
    return anagram_pairs <= 416