def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            normalized = normalize(s)
            anagram_dict.setdefault(normalized, 0)
            anagram_dict[normalized] += 1
    count = sum((1 for v in anagram_dict.values() if v > 1))
    return count <= 255