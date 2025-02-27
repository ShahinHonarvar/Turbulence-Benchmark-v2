def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3 and key.isalpha():
            anagrams[key] = anagrams.get(key, 0) + 1
    return max(anagrams.values(), default=0) <= 4