def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        key = normalize(string)
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    pairs = 0
    for key in anagrams:
        pairs += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return pairs <= 19