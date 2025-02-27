from collections import Counter

def if_contains_anagrams(lst):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sorted_string(lst[i]) == sorted_string(lst[j])):
                anagram_count += 1
    return anagram_count >= 88