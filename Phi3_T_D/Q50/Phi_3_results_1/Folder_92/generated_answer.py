def if_contains_anagrams(lst):

    def normalized(s):
        return ''.join(sorted(s.lower()))
    seen = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            norm1 = normalized(lst[i])
            norm2 = normalized(lst[j])
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (norm1 == norm2):
                seen.add(norm1)
            if len(seen) >= 2:
                return True
    return False