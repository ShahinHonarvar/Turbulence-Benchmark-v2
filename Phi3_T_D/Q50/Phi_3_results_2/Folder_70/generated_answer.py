from collections import Counter

def if_contains_anagrams(strings):
    count_anagrams = 0
    for i in range(len(strings)):
        word = sorted(strings[i].lower())
        for j in range(i + 1, len(strings)):
            if Counter(word) == Counter(sorted(strings[j].lower())) and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                count_anagrams += 1
    return count_anagrams >= 189