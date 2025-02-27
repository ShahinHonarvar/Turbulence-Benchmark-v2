def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def has_three_or_more_characters(s):
        return len(s) >= 3
    count = 0
    normalized = {}
    for s in strings:
        if has_three_or_more_characters(s):
            norm = normalize(s)
            if norm in normalized:
                count += normalized[norm]
                normalized[norm] += 1
            else:
                normalized[norm] = 1
    return count >= 194