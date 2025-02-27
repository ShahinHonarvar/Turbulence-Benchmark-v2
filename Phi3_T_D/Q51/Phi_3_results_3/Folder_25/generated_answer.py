def if_contains_anagrams(lst):
    anagrams_count = 0
    lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    seen = set()
    for s in lst:
        if s in seen:
            anagrams_count += 1
        seen.add(s)
    return anagrams_count <= 67