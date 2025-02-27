def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        for t in strings:
            sorted_t = ''.join(sorted(t.lower()))
            if sorted_s == sorted_t and s != t:
                anagrams.append((s, t))
    return len(anagrams) >= 153