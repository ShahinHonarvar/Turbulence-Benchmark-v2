def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def count_anagrams(normalized):
        counts = {}
        for s in normalized:
            counts[s] = counts.get(s, 0) + 1
        return sum((count for count in counts.values() if count >= 2))
    normalized_strings = [normalize(s) for s in strings]
    valid_count = 0
    for string in normalized_strings:
        if len(string) >= 3:
            valid_count += count_anagrams([s for s in normalized_strings if s == string]) // 2
    return valid_count >= 21