def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and (len(s2) >= 3)
    pairs = [(s1, s2) for i, s1 in enumerate(strings) for j, s2 in enumerate(strings) if i < j and is_anagram(s1, s2)]
    return len(pairs) <= 46