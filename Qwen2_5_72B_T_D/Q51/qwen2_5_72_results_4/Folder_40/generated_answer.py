def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            norm = normalize(s)
            anagram_counts[norm] = anagram_counts.get(norm, 0) + 1
    pairs = 0
    for count in anagram_counts.values():
        pairs += count * (count - 1) // 2
    return pairs <= 29