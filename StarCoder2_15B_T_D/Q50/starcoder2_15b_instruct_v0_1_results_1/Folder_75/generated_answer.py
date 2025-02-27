def if_contains_anagrams(strings):
    anagrams = []
    for i, s in enumerate(strings):
        for t in strings[i + 1:]:
            if sorted(s.lower()) == sorted(t.lower()) and len(s) >= 3 and (len(t) >= 3):
                anagrams.append((s, t))
    return len(anagrams) >= 70