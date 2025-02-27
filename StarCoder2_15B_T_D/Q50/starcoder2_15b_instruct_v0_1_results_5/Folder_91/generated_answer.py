def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return len(list(filter(lambda x: len(x) >= 6, anagrams.values()))) > 0