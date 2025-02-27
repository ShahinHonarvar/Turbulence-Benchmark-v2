def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for item in lst:
        if len(item) >= 3 and item.isalpha():
            normalized = normalize(item)
            anagram_dict[normalized] = anagram_dict.get(normalized, 0) + 1
    anagram_pairs = sum((1 for count in anagram_dict.values() if count > 1))
    return anagram_pairs <= 2