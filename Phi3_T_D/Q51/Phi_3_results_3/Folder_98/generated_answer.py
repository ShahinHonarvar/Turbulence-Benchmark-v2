def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def count_anagrams(sl):
        anagrams = {}
        for s in sl:
            n = normalize(s)
            if n in anagrams:
                anagrams[n].append(s)
            else:
                anagrams[n] = [s]
        pairs = sum([len(strings) - len(entries) for entries in anagrams.values() if len(entries) > 1])
        return pairs // 2
    total_pairs = count_anagrams([s for s in strings if len(s) >= 3])
    return total_pairs <= 46