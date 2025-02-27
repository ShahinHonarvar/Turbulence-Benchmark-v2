def if_contains_anagrams(lst):
    return len([(x, y) for x in lst for y in lst if x != y and len(x) == len(y) >= 3 and (sorted(x.lower()) == sorted(y.lower()))]) <= 93