def if_contains_anagrams(words):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    count = {}
    for word in words:
        if len(word) >= 3:
            canon = canonical_form(word)
            if canon in count:
                count[canon] += 1
            else:
                count[canon] = 1
    anagram_pairs = sum((c * (c - 1) // 2 for c in count.values()))
    return anagram_pairs >= 411