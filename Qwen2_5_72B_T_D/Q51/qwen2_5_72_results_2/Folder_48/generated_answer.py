from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if Counter(lst[i]) == Counter(lst[j]):
                anagram_pairs += 1
    return anagram_pairs <= 277