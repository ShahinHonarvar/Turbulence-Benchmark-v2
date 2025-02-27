def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_dict[normalized] = anagram_dict.get(normalized, 0) + 1
    count = sum((1 for count in anagram_dict.values() if count > 1))
    return count >= 39