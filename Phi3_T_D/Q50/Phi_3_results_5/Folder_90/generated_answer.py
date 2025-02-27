def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    normalized = {}
    for s in strings:
        if len(s) >= 3:
            key = normalize(s)
            if key in normalized:
                count += normalized[key]
                normalized[key] += 1
            else:
                normalized[key] = 1
    return count >= 177