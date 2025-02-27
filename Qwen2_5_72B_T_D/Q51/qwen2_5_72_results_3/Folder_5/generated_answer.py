def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = {}
    for word in lst:
        if len(word) >= 3:
            normalized = normalize(word)
            if normalized in count:
                count[normalized] += 1
            else:
                count[normalized] = 1
    anagram_pairs = sum((1 for c in count.values() if c > 1))
    return anagram_pairs <= 4