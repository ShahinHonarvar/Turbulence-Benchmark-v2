def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for i, s1 in enumerate(string_list):
        for j in range(i + 1, len(string_list)):
            s2 = string_list[j]
            if sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and (len(s2) >= 3):
                anagram_pairs += 1
                if anagram_pairs > 35:
                    return False
    return anagram_pairs <= 35