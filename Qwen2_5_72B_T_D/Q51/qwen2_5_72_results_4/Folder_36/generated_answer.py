def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    anagram_count = {}
    for s in strings:
        if len(s) < 3:
            continue
        norm = normalize(s)
        if norm in anagram_count:
            for prev in anagram_count[norm]:
                anagram_pairs.add(tuple(sorted((s, prev))))
            anagram_count[norm].append(s)
        else:
            anagram_count[norm] = [s]
    return len(anagram_pairs) <= 25