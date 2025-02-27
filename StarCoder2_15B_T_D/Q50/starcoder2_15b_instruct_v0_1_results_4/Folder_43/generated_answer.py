def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_counts = {}
    for s1 in strings:
        for s2 in strings:
            if s1 != s2 and are_anagrams(s1, s2):
                sorted_pair = tuple(sorted([s1, s2]))
                anagram_counts[sorted_pair] = anagram_counts.get(sorted_pair, 0) + 1
    return any((count >= 61 for count in anagram_counts.values()))