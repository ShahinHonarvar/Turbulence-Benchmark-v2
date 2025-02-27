def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if word in anagrams:
                anagrams[word] += 1
            else:
                anagrams[word] = 1
    return max(anagrams.values()) <= 318