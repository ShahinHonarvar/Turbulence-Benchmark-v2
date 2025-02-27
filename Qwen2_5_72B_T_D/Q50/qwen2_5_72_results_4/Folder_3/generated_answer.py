def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            anagram_dict[normalized] = anagram_dict.get(normalized, 0) + 1
    anagram_count = sum((1 for count in anagram_dict.values() if count > 1))
    return anagram_count >= 30