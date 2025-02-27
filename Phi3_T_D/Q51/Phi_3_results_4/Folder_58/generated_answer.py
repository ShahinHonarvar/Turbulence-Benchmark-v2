def if_contains_anagrams(strings):
    count = 0
    seen = set()
    strings = [s.lower().replace(' ', '') for s in strings]
    for s in strings:
        s_key = ''.join(sorted(s))
        if s_key in seen:
            count += 1
        else:
            seen.add(s_key)
    return count <= 60