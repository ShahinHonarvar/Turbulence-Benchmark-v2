from collections import Counter

def if_contains_anagrams(strings):

    def count_anagrams(lst):
        d = {}
        for s in lst:
            if len(s) >= 3:
                s = ''.join(sorted(s.lower()))
                if s in d:
                    d[s] += 1
                else:
                    d[s] = 1
        return sum((v * (v - 1) // 2 for v in d.values()))
    return count_anagrams(strings) <= 58