def if_contains_anagrams(strings):
    counts = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        counts[key] = counts.get(key, 0) + 1
    return any((count >= 69 for count in counts.values()))