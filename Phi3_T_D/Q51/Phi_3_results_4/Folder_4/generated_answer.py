from collections import Counter

def if_contains_anagrams(lst):

    def normalize(s):
        return Counter(s.lower())
    lst = [s for s in lst if len(s) >= 3]
    count = Counter([normalize(s) for s in lst])
    return sum((val * (val - 1) // 2 for val in count.values())) <= 84