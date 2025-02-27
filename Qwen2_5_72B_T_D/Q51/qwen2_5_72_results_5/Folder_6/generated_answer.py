def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            norm = normalize(word)
            anagrams[norm] = anagrams.get(norm, 0) + 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs_count <= 86