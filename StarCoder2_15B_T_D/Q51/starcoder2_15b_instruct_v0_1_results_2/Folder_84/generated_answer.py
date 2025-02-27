def if_contains_anagrams(input_list):

    def is_anagram(s1, s2):
        s1 = sorted(s1.lower())
        s2 = sorted(s2.lower())
        if len(s1) != len(s2):
            return False
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                return False
        return True
    anagram_pairs = []
    for i, s1 in enumerate(input_list):
        for s2 in input_list[i + 1:]:
            if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
                anagram_pairs.append((s1, s2))
    return len(anagram_pairs) <= 16