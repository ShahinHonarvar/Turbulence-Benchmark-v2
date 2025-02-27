def if_contains_anagrams(lst):

    def to_tuple(s):
        return tuple(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            key = to_tuple(word)
            if key in anagram_dict:
                anagram_dict[key] += 1
            else:
                anagram_dict[key] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs >= 72