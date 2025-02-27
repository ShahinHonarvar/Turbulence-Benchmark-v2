def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and (len(s2) >= 3)
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i], lst[j]):
                anagrams_count += 1
    return anagrams_count <= 289