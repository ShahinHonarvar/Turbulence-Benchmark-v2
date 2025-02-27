def if_contains_anagrams(lst):
    lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    return any((lst.count(s) > 1 for s in set(lst))) and sum((lst.count(s) - 1 for s in set(lst))) >= 11