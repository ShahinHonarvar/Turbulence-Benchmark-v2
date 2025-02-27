def if_contains_anagrams(string_list):

    def are_anagrams(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2))
    anagrams_pairs = [(s1, s2) for i, s1 in enumerate(string_list) for s2 in string_list[i + 1:] if are_anagrams(s1, s2)]
    return len(anagrams_pairs) <= 50