def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[key] = anagrams.get(key, 0) + 1
    return sum((count > 1 for count in anagrams.values())) >= 30