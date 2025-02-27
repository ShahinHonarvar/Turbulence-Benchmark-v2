def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    lst_lower = [s.lower() for s in lst if len(s) >= 3]
    for i in range(len(lst_lower)):
        for j in range(i + 1, len(lst_lower)):
            if is_anagram(lst_lower[i], lst_lower[j]):
                count += 1
    return count >= 93