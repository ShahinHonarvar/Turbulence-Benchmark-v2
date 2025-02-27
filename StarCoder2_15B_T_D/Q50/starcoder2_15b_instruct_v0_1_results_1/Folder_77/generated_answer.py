def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        canonical = ''.join(sorted(word.lower()))
        if canonical not in anagrams:
            anagrams[canonical] = [word]
        else:
            anagrams[canonical].append(word)
    return any((len(words) >= 2 for words in anagrams.values()))