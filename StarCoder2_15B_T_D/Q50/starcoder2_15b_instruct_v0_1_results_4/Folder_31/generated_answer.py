def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word.lower()))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return len([pair for pair in anagrams.values() if len(pair) >= 3]) >= 68