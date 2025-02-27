def if_contains_anagrams(strings):
    sorted_anagrams = {}
    for s in strings:
        if 3 <= len(s) <= 28:
            assorted = ''.join(sorted(s.lower()))
            sorted_anagrams[assorted] = sorted_anagrams.get(assorted, 0) + 1
    return sum((1 for x in sorted_anagrams.values() if x > 1 <= 28))