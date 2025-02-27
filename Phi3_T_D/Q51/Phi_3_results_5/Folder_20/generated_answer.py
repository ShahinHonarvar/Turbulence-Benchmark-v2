def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            key = normalize(s)
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    count_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values() if len(lst) > 1))
    return count_pairs <= 131