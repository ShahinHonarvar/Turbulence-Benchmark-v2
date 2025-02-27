from itertools import combinations

def if_contains_anagrams(strings):
    count = 0
    for a, b in combinations(strings, 2):
        if len(a) >= 3 and len(b) >= 3:
            a_sorted = sorted(a.lower())
            b_sorted = sorted(b.lower())
            if a_sorted == b_sorted:
                count += 1
                if count > 44:
                    return False
    return True