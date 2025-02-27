from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            for i in range(len(lst)):
                if i != lst.index(s) and sorted_s == ''.join(sorted(lst[i].lower())):
                    count += 1
    return count <= 210