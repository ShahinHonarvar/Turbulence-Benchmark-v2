def if_contains_anagrams(lst):

    def to_key(s):
        return ''.join(sorted(s.lower()))
    count = {}
    for word in lst:
        if len(word) >= 3:
            key = to_key(word)
            if key in count:
                count[key] += 1
            else:
                count[key] = 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs >= 47