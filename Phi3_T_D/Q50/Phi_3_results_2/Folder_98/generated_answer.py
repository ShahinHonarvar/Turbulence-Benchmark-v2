def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    normalized_strings = [normalize(s) for s in strings if len(s) >= 3]
    seen = set()
    for ns in normalized_strings:
        if ns in seen:
            count += 1
            if count >= 7:
                return True
        seen.add(ns)
    return False