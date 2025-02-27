def if_contains_anagrams(lst):
    anagrams = []
    for i, s in enumerate(lst):
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            for j in range(i + 1, len(lst)):
                if sorted_s == ''.join(sorted(lst[j].lower())):
                    anagrams.append((s, lst[j]))
    return len(anagrams) >= 68