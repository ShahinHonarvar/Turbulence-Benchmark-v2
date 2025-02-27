def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = {}
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            norm = normalize(s)
            if norm in anagram_pairs:
                anagram_pairs[norm].append(s)
            else:
                anagram_pairs[norm] = [s]
    pair_count = sum((len(anagrams) - 1 for anagrams in anagram_pairs.values() if len(anagrams) > 1))
    return pair_count <= 34