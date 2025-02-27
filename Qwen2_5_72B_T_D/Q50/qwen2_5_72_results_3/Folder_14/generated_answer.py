def if_contains_anagrams(lst):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    count = {}
    for word in lst:
        if len(word) >= 3:
            canon = canonical_form(word)
            if canon in count:
                count[canon] += 1
            else:
                count[canon] = 1
    anagram_pairs = sum((k * (k - 1) // 2 for k in count.values()))
    return anagram_pairs >= 22