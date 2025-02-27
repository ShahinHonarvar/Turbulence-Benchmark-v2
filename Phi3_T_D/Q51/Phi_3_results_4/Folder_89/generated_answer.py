def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    seen = set()
    for s in strings:
        if len(s) < 3:
            continue
        norm = normalize(s)
        if norm in seen:
            count += 1
        seen.add(norm)
    return count <= 73