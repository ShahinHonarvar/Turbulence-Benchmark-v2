def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return len(set(s1.lower()) - set(s2.lower())) <= len(s1) - len(s2)
    count_anagrams = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if are_anagrams(strings[i], strings[j]):
                    count_anagrams += 1
    return count_anagrams <= 75