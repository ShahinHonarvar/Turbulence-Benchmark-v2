def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    lst = [s.lower() for s in lst if len(s) >= 3]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i], lst[j]):
                count += 1
                if count >= 219:
                    return True
    return False