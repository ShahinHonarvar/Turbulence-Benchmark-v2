def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        lower_word = word.lower()
        key = ''.join(sorted(lower_word))
        if len(lower_word) >= 3:
            if key in anagrams:
                anagrams[key].append(lower_word)
            else:
                anagrams[key] = [lower_word]
    return sum((len(v) - 1 for v in anagrams.values())) >= 81