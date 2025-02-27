def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagrams = {}
    for word in words:
        if len(word) >= 3:
            norm_word = normalize(word)
            if norm_word in anagrams:
                anagrams[norm_word].append(word)
            else:
                anagrams[norm_word] = [word]
    count = 0
    for words in anagrams.values():
        if len(words) > 1:
            count += len(words) * (len(words) - 1) // 2
    return count >= 106