from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_pairs = sum((1 for i in range(len(lst)) for j in range(i + 1, len(lst)) if is_anagram(lst[i], lst[j])))
    return anagram_pairs <= 65