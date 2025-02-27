def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())
    count_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                count_pairs += 1
                if count_pairs > 29:
                    return False
    return True