def if_contains_anagrams(words):
    anagrams = dict()
    for word in words:
        word_key = ''.join(sorted(word.lower()))
        if len(word_key) >= 3:
            if word_key not in anagrams:
                anagrams[word_key] = [word]
            else:
                anagrams[word_key].append(word)
    return len(anagrams) <= 392