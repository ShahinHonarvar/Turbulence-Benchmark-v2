def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    lst = [s.lower() for s in lst if len(s) >= 3 and s.isalpha()]
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_pairs += 1
                if anagram_pairs > 22:
                    return False
    return True