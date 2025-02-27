def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            normalized = normalize(s)
            anagram_dict[normalized] = anagram_dict.get(normalized, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs <= 41