def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        key = tuple(sorted(word.lower()))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return len(anagrams) <= 35