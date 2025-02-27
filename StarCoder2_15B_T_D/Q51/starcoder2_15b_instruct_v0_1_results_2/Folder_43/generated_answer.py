def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        canonical_word = ''.join(sorted(word.lower()))
        if canonical_word in anagrams:
            anagrams[canonical_word].append(word)
        else:
            anagrams[canonical_word] = [word]
    return len([pair for pair in anagrams.values() if len(pair) > 1]) <= 3