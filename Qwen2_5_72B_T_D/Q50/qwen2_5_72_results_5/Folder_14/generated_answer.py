def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    strings = [s for s in strings if len(s) >= 3]
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if are_anagrams(strings[i], strings[j]):
                count += 1
                if count >= 22:
                    return True
    return False