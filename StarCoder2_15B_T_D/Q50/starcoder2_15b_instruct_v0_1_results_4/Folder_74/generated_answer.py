def if_contains_anagrams(words):

    def anagram_key(word):
        return tuple(sorted(word.lower()))
    anagrams = {}
    for word in words:
        key = anagram_key(word)
        if key not in anagrams:
            anagrams[key] = [word]
        else:
            anagrams[key].append(word)
    return any((len(anagrams[key]) >= 17 for key in anagrams if len(key) >= 3))