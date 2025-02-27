def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = {}
    for s in strings:
        if len(s) >= 3:
            key = normalize(s)
            count[key] = count.get(key, 0) + 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs <= 6