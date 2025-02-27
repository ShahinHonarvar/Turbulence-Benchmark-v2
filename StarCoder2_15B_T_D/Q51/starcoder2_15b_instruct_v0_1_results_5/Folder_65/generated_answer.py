def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    num_anagrams = sum((len(v) - 1 for v in anagrams.values()))
    return num_anagrams <= 72