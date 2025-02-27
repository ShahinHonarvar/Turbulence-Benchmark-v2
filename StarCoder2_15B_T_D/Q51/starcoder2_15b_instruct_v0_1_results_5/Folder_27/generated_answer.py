def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        s1 = ''.join((c for c in s1 if c.isalpha())).lower()
        s2 = ''.join((c for c in s2 if c.isalpha())).lower()
        return sorted(s1) == sorted(s2) and len(s1) >= 3 and (len(s2) >= 3)
    num_anagrams = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                num_anagrams += 1
    return num_anagrams <= 113