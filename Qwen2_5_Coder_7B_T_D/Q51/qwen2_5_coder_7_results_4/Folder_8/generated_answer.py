from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(a, b):
        return Counter(a.lower()) == Counter(b.lower())
    anagram_pairs = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                anagram_pairs += 1
    return anagram_pairs <= 68