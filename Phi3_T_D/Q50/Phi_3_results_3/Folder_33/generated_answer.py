def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and (len(s2) >= 3)
    anagram_pairs = [(s1, s2) for i, s1 in enumerate(string_list) for s2 in string_list[i + 1:] if is_anagram(s1, s2)]
    return len(anagram_pairs) >= 140