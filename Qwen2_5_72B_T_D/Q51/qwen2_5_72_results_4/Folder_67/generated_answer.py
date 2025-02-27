def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagrams = {}
    for word in words:
        if len(word) >= 3 and word.isalpha():
            normalized = normalize(word)
            if normalized in anagrams:
                anagrams[normalized].append(word)
            else:
                anagrams[normalized] = [word]
    count = sum((1 for group in anagrams.values() if len(group) > 1))
    return count <= 5