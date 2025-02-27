def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        norm = normalize(s)
        anagrams.setdefault(norm, []).append(s)
    pair_count = 0
    for key in anagrams:
        pairs = sum((1 for i in range(len(anagrams[key])) for j in range(i + 1, len(anagrams[key]))))
        pair_count += pairs
    return pair_count >= 58