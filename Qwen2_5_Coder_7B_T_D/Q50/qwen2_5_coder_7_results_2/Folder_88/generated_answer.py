def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2) and len(s1) >= 3
    lower_lst = [s.lower() for s in lst]
    anagram_pairs = 0
    for i in range(len(lower_lst)):
        for j in range(i + 1, len(lower_lst)):
            if is_anagram(lower_lst[i], lower_lst[j]):
                anagram_pairs += 1
                if anagram_pairs >= 34:
                    return True
    return False