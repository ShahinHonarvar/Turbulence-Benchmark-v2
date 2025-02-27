def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_counts = {}
    for s in strings:
        if len(s) >= 3:
            for s2 in strings:
                if are_anagrams(s, s2):
                    anagram_counts[s] = anagram_counts.get(s, 0) + 1
    return max(anagram_counts.values(), default=0) <= 289