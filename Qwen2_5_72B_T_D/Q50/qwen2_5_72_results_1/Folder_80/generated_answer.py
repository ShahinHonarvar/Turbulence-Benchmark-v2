def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = {}
    for word in words:
        if len(word) >= 3:
            norm = normalize(word)
            if norm in count:
                count[norm] += 1
            else:
                count[norm] = 1
    anagram_pairs = sum((1 for v in count.values() if v > 1))
    return anagram_pairs >= 19