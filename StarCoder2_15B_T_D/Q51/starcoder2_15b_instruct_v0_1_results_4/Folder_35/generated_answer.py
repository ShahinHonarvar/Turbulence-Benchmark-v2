def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        s1 = sorted(s1.lower())
        s2 = sorted(s2.lower())
        return s1 == s2
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_pairs += 1
                if anagram_pairs > 210:
                    return False
    return True