from itertools import combinations

def if_contains_anagrams(strings):
    count = 0
    for a, b in combinations(strings, 2):
        if len(a) < 3 or len(b) < 3:
            continue
        if sorted(a.lower()) == sorted(b.lower()):
            count += 1
    return count >= 59