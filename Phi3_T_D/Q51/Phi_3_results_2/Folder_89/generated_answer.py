def if_contains_anagrams(strings):

    def get_canonical(s):
        return ''.join(sorted(s.lower()))
    canonical_counts = {}
    for string in strings:
        canonical = get_canonical(string)
        if len(string) >= 3:
            canonical_counts[canonical] = canonical_counts.get(canonical, 0) + 1
    anagram_pairs = sum((v - 1 for v in canonical_counts.values() if v > 1))
    return anagram_pairs <= 73