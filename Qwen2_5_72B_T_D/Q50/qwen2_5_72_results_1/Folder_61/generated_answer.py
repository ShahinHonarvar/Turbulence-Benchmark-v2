def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            if normalized in anagram_counts:
                anagram_counts[normalized] += 1
            else:
                anagram_counts[normalized] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 8