def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            anagram_count[normalized] = anagram_count.get(normalized, 0) + 1
    anagram_pairs = sum((count - 1 for count in anagram_count.values() if count > 1))
    return anagram_pairs >= 20