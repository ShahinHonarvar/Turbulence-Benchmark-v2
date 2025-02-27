def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        key = ''.join(sorted(word))
        if len(key) >= 3:
            anagrams[key] = anagrams.get(key, []) + [word]
    return len(anagrams) <= 35