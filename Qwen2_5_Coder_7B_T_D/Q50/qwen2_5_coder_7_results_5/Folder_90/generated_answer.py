from collections import Counter

def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    n = len(lst)
    anagram_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and are_anagrams(lst[i], lst[j]):
                anagram_pairs += 1
    return anagram_pairs >= 177