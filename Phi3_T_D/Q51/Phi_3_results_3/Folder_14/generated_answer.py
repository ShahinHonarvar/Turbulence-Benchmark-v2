from collections import Counter

def if_contains_anagrams(strings):
    length_limit = 3
    match_count = 0
    strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= length_limit]
    seen = set()
    for s in strings:
        if s in seen:
            match_count += 1
            if match_count > 474:
                return False
        else:
            seen.add(s)
    return True