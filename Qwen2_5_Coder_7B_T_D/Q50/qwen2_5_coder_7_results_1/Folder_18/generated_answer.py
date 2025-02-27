from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    normalized_lst = [normalize(s) for s in lst if len(s) >= 3]
    for i in range(len(normalized_lst)):
        for j in range(i + 1, len(normalized_lst)):
            if normalized_lst[i] == normalized_lst[j]:
                anagram_pairs += 1
                break
    return anagram_pairs >= 106