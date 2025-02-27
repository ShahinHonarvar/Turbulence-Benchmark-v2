from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagram_count:
                anagram_count[sorted_s] += 1
            else:
                anagram_count[sorted_s] = 1
    for count in anagram_count.values():
        if count > 1:
            anagram_count += count - 1
    return anagram_count <= 206