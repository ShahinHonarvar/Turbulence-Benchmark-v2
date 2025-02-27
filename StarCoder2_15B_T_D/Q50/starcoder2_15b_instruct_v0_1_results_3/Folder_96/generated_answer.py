def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            if key not in anagrams:
                anagrams[key] = [s]
            else:
                anagrams[key].append(s)
    count = 0
    for v in anagrams.values():
        count += len(v) // 2
    return count >= 98