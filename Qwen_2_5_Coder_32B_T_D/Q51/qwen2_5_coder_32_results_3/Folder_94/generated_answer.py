from collections import Counter

def if_contains_anagrams(lst):
    s = set()
    count = 0
    for word in lst:
        w = word.lower()
        if len(w) >= 3:
            c = str(sorted(Counter(w).items()))
            if c in s:
                count += 1
                if count > 181:
                    return False
            else:
                s.add(c)
    return True