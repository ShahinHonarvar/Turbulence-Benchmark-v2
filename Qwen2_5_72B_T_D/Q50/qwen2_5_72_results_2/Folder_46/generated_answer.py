def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    lst_lower = [s.lower() for s in lst if len(s) >= 3]
    count = 0
    for i in range(len(lst_lower)):
        for j in range(i + 1, len(lst_lower)):
            if are_anagrams(lst_lower[i], lst_lower[j]):
                count += 1
            if count >= 38:
                return True
    return False