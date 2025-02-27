def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        if len(s1) != len(s2) or len(s1) < 3:
            return False
        return sorted(s1) == sorted(s2)
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                count += 1
                if count > 77:
                    return False
    return True