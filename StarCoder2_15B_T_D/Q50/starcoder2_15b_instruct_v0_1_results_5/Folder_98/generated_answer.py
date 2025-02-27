def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        canonical_word = ''.join(sorted(word.lower()))
        if canonical_word in anagrams:
            anagrams[canonical_word].append(word)
        else:
            anagrams[canonical_word] = [word]
    return any((len(words) >= 7 for words in anagrams.values()))