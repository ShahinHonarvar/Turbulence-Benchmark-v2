from collections import Counter

def if_contains_anagrams(lst):

    def count_anagrams(s):
        return sum(Counter(s).values()) >= 3
    lst = [sorted(s.lower()) for s in lst if count_anagrams(s)]
    return len(lst) >= 41