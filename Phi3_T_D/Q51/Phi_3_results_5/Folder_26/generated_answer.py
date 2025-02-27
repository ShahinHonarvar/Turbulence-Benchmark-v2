def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    seen = set()
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        norm = normalize(s)
        for k in seen:
            if norm == k:
                count += 1
                if count > 35:
                    return False
                break
        seen.add(norm)
    return True