def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            normalized = normalize(s)
            anagram_counts[normalized] = anagram_counts.get(normalized, 0) + 1
    num_pairs = 0
    for count in anagram_counts.values():
        num_pairs += count * (count - 1) // 2
    return num_pairs <= 49