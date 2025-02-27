def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        if len(s) >= 3 and s.lower() in anagrams:
            return True
        for t in strings:
            if s != t and sorted(s.lower()) == sorted(t.lower()):
                anagrams.add(s.lower())
    return len(anagrams) <= 188