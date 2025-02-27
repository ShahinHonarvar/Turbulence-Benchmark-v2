def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    length_counts = {}
    for s in strings:
        n = len(s)
        if n >= 3:
            norm = normalize(s[n // 2:])
            if norm in length_counts:
                length_counts[norm] += 1
                count += 1
            else:
                length_counts[norm] = 1
    return count >= 55