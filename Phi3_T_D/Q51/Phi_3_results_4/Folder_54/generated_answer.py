def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def count_anagram_pairs(normalized_strings):
        anagram_count = {}
        for norm in normalized_strings:
            if len(norm) < 3:
                continue
            anagram_count[norm] = anagram_count.get(norm, 0) + 1
        return sum((count * (count - 1) // 2 for count in anagram_count.values()))
    normalized = [normalize(s) for s in strings]
    return count_anagram_pairs(normalized) <= 39