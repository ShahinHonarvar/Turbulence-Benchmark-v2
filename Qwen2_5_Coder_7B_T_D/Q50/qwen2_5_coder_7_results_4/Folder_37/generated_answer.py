from collections import Counter

def if_contains_anagrams(lst):

    def count_anagrams(s):
        return Counter(sorted(s.lower()))
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if count_anagrams(lst[i]) == count_anagrams(lst[j]) and len(lst[i]) >= 3:
                anagram_pairs += 1
    return anagram_pairs >= 29