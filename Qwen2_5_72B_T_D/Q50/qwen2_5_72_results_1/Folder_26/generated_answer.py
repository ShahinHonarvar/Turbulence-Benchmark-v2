def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_dict[normalized] = anagram_dict.get(normalized, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs >= 49