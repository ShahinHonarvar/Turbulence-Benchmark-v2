def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if key not in anagrams:
            anagrams[key] = [s]
        else:
            anagrams[key].append(s)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1 and len(key) >= 3:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 91