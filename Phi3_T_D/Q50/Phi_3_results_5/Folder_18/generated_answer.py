def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    pairs = 0
    seen = set()
    for sorted_string in sorted_strings:
        if sorted_string in seen:
            pairs += 1
        else:
            seen.add(sorted_string)
        if pairs >= 106:
            return True
    return False