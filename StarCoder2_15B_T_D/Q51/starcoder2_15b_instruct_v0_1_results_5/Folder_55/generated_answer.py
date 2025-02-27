def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        key = ''.join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return len(list(filter(lambda x: len(x) > 1, anagrams.values()))) <= 44