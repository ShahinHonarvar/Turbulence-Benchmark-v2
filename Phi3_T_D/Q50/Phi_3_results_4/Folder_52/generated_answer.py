def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    count = 0
    already_seen = set()
    for item in lst:
        normalized = normalize_string(item)
        if len(normalized) < 3:
            continue
        if normalized in already_seen:
            count += 1
            if count >= 58:
                return True
        else:
            already_seen.add(normalized)
    return False