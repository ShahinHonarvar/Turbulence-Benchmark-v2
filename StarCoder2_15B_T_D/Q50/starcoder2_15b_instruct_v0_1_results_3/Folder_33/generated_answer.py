def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3
    anagrams = {}
    for s in strings:
        for t in strings:
            if s != t and are_anagrams(s, t):
                if s in anagrams:
                    anagrams[s].append(t)
                else:
                    anagrams[s] = [t]
    return len(anagrams) >= 140