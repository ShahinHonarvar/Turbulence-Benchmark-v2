def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    lst_lower = [s.lower() for s in lst if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(lst_lower)):
        for j in range(i + 1, len(lst_lower)):
            if are_anagrams(lst_lower[i], lst_lower[j]):
                anagram_pairs += 1
    return anagram_pairs >= 277