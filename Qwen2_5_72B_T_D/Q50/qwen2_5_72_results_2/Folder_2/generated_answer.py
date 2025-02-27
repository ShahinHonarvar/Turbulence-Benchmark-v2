def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = {}
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            if normalized in count:
                count[normalized] += 1
            else:
                count[normalized] = 1
    anagram_pairs = sum((c * (c - 1) // 2 for c in count.values()))
    return anagram_pairs >= 246