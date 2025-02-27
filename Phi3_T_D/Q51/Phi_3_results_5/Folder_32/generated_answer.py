def if_contains_anagrams(strings):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        key = normalize_string(string)
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    pairs_count = sum((len(v) // 2 for v in anagrams.values()))
    return pairs_count <= 89