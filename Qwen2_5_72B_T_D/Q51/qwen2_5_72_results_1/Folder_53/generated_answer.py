def if_contains_anagrams(lst):

    def to_sorted_tuple(s):
        return tuple(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            sorted_tuple = to_sorted_tuple(word)
            anagram_dict.setdefault(sorted_tuple, []).append(word)
    anagram_count = sum((len(v) > 1 for v in anagram_dict.values()))
    return anagram_count <= 8