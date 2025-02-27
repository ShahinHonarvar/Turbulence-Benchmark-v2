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
    count = 0
    for key in anagrams:
        pairs = len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
        count += pairs
    return count >= 91