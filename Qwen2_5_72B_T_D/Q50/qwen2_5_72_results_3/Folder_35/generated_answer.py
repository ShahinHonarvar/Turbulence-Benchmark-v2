def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        return sorted(s1) == sorted(s2)
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i].lower(), lst[j].lower()):
                count += 1
    return count >= 153