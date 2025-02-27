def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return len(s1) == len(s2) and sorted(s1) == sorted(s2)
    count_anagrams = 0
    lst_lower = [s.lower() for s in lst]
    length = len(lst_lower)
    for i in range(length):
        for j in range(i + 1, length):
            if are_anagrams(lst_lower[i], lst_lower[j]):
                count_anagrams += 1
                if count_anagrams > 67:
                    return False
    return True