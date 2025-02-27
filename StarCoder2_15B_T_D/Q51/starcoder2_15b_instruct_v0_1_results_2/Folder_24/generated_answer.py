def if_contains_anagrams(strings):
    counts = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            key = ''.join(sorted(s))
            counts[key] = counts.get(key, 0) + 1
    return max(counts.values()) <= 96