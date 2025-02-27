def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for word in lst:
        if len(word) < 3:
            continue
        norm = normalize(word)
        if norm in anagrams:
            anagrams[norm].append(word)
        else:
            anagrams[norm] = [word]
    pairs = 0
    for key in anagrams:
        pairs += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
        if pairs > 43:
            return False
    return True