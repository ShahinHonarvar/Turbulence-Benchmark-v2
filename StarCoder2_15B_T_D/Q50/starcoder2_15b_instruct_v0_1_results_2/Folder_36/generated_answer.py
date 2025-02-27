def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return sorted(s1) == sorted(s2)
    anagrams = {}
    for s in strings:
        for s2 in strings:
            if s != s2 and len(s) >= 3 and (len(s2) >= 3) and are_anagrams(s, s2):
                if s not in anagrams:
                    anagrams[s] = []
                anagrams[s].append(s2)
    return len(anagrams) >= 312