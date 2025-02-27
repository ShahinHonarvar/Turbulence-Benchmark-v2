def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    strings = [s.lower() for s in strings if len(s) >= 3]
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                count += 1
                if count >= 28:
                    return True
    return False