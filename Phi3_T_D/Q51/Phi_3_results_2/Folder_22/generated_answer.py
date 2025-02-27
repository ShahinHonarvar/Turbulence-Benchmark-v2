def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    normalized_lst = [normalize(s) for s in lst if len(s) >= 3]
    seen = set()
    count = 0
    for s in normalized_lst:
        if s in seen:
            count += 1
        else:
            seen.add(s)
    return count <= 14