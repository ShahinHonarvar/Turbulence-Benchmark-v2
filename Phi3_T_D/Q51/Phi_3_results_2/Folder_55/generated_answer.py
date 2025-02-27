def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    seen = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        key = normalize(s)
        if key in seen:
            count += seen[key]
            seen[key] += 1
        else:
            seen[key] = 1
    return count <= 44