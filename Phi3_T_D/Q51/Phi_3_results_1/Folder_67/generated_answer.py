def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings]
    seen = {}
    for s in sorted_strings:
        if s in seen:
            seen[s] += 1
            if seen[s] > 2:
                return False
        else:
            seen[s] = 1
    return True