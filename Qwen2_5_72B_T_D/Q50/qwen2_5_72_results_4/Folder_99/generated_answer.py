def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        return sorted(s1) == sorted(s2)
    lst_lower = [s.lower() for s in lst]
    anagram_count = 0
    for i in range(len(lst_lower)):
        for j in range(i + 1, len(lst_lower)):
            if are_anagrams(lst_lower[i], lst_lower[j]):
                anagram_count += 1
                if anagram_count >= 314:
                    return True
    return False