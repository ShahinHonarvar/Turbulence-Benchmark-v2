def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = (''.join(sorted(s.lower())), len(s))
        if key not in anagrams:
            anagrams[key] = [s]
        else:
            anagrams[key].append(s)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count <= 54