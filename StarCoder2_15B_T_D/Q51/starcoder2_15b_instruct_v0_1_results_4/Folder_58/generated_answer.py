def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            canonical_word = ''.join(sorted(word))
            if canonical_word in anagrams:
                anagrams[canonical_word].append(word)
            else:
                anagrams[canonical_word] = [word]
    return len(anagrams) <= 60