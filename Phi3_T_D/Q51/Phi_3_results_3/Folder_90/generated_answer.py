def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            normalized = normalize(string)
            anagrams.setdefault(normalized, []).append(string)
    pairs = sum((len(ana) * (len(ana) - 1) // 2 for ana in anagrams.values() if len(ana) > 1))
    return pairs <= 147