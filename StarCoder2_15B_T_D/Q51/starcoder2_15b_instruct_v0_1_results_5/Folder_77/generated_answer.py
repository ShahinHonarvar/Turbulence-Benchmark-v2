def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        s1 = ''.join((c for c in s1.lower() if c.isalpha()))
        s2 = ''.join((c for c in s2.lower() if c.isalpha()))
        return sorted(s1) == sorted(s2)
    anagram_counts = {}
    for s in strings:
        anagram_counts[s] = sum((are_anagrams(s, other_s) for other_s in strings))
    return all((count <= 17 for count in anagram_counts.values()))