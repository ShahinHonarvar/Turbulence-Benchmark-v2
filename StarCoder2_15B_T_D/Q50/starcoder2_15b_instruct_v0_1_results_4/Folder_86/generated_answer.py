def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        canonical_word = ''.join(sorted(word.lower()))
        if canonical_word in anagrams:
            anagrams[canonical_word].append(word)
        else:
            anagrams[canonical_word] = [word]
    return any((len(anagrams[canonical_word]) >= 115 for canonical_word in anagrams))