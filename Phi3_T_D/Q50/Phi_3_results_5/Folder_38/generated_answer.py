def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                count += 1
                if count >= 24:
                    return True
    return False