def if_contains_anagrams(strings):
    count = 0
    seen = {}
    for s in strings:
        sorted_s = str(sorted(s.lower()))
        if sorted_s in seen:
            count += 1
        else:
            seen[sorted_s] = True
    if count <= 86:
        return True
    return False