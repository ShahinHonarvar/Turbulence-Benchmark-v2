def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counts = {}
    for s in strings:
        if len(s) >= 3:
            n = normalize(s)
            counts[n] = counts.get(n, 0) + 1
    anagram_pairs = sum((count // 2 for count in counts.values()))
    return anagram_pairs >= 88