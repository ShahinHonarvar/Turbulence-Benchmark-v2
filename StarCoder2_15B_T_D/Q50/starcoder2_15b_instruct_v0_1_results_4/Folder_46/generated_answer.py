def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            canonical_form = ''.join(sorted(word))
            anagrams[canonical_form] = anagrams.get(canonical_form, []) + [word]
    return any((len(v) >= 38 for v in anagrams.values()))