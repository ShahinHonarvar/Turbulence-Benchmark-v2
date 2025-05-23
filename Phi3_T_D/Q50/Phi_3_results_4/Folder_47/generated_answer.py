def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    length = len(strings)
    count = 0
    for i in range(length):
        for j in range(i + 1, length):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if are_anagrams(strings[i], strings[j]):
                    count += 1
                    if count >= 47:
                        return True
    return False