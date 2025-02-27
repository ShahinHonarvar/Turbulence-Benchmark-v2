def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        normalized = ''.join(sorted(s.lower()))
        if normalized not in anagrams:
            anagrams[normalized] = []
        anagrams[normalized].append(s)
    count = 0
    for key, value in anagrams.items():
        if len(value) > 1 and len(key) >= 3:
            count += len(value) * (len(value) - 1) // 2
    return count >= 26