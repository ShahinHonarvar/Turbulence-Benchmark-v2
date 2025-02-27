def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and are_anagrams(strings[i], strings[j]):
                count += 1
    return count >= 16