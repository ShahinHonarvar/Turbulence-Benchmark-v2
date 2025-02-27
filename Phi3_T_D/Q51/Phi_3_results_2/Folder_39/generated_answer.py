def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            if norm in anagrams:
                anagrams[norm].append(s)
            else:
                anagrams[norm] = [s]
    pairs = 0
    for anagram_list in anagrams.values():
        pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return pairs <= 257