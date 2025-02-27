from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i].lower(), lst[j].lower()):
                anagram_pairs.add((lst[i].lower(), lst[j].lower()))
    return len(anagram_pairs) <= 84