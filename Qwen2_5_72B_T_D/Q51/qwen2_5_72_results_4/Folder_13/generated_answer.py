from collections import defaultdict

def if_contains_anagrams(strings):

    def count_anagrams(lst):
        d = defaultdict(int)
        for s in lst:
            if len(s) >= 3:
                s = ''.join(sorted(s.lower()))
                d[s] += 1
        return sum((v * (v - 1) // 2 for v in d.values()))
    return count_anagrams(strings) <= 54