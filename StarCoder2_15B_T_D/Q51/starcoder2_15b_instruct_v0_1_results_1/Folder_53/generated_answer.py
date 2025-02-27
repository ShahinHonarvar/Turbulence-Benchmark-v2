def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1 = ''.join((c for c in s1.lower() if c.isalpha()))
        s2 = ''.join((c for c in s2.lower() if c.isalpha()))
        return sorted(s1) == sorted(s2)
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            for s2 in strings:
                if is_anagram(s, s2):
                    anagrams[s] = anagrams.get(s, 0) + 1
    return max(anagrams.values(), default=0) <= 8