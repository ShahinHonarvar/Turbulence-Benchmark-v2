def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            norm = normalize(word)
            anagrams[norm] = anagrams.get(norm, 0) + 1
    count = sum((1 for count in anagrams.values() if count > 1))
    return count <= 30