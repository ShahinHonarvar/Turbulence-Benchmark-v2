def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            anagram_dict[norm] = anagram_dict.get(norm, 0) + 1
    anagram_count = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_count <= 57