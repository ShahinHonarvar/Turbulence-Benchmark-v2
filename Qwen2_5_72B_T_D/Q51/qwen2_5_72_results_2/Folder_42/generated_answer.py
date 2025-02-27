from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    lst_lower = [s.lower() for s in lst if len(s) >= 3]
    anagram_pairs = set()
    for i in range(len(lst_lower)):
        for j in range(i + 1, len(lst_lower)):
            if is_anagram(lst_lower[i], lst_lower[j]):
                anagram_pairs.add((lst_lower[i], lst_lower[j]))
    return len(anagram_pairs) <= 38