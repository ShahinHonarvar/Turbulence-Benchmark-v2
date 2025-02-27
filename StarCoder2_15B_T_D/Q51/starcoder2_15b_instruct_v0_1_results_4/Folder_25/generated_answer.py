def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word_key = ''.join(sorted(word.lower()))
        if len(word_key) >= 3:
            if word_key in anagrams:
                anagrams[word_key].append(word)
            else:
                anagrams[word_key] = [word]
    num_anagrams = sum((len(v) - 1 for v in anagrams.values()))
    return num_anagrams <= 67