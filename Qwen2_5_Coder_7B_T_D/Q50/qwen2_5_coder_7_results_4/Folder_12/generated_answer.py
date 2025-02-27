from collections import Counter

def if_contains_anagrams(lst):

    def count_anagrams(s):
        return Counter(sorted(s.lower()))
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (count_anagrams(lst[i]) == count_anagrams(lst[j])):
                anagram_count += 1
    return anagram_count >= 69