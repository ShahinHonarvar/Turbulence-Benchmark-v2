def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for i, string1 in enumerate(string_list):
        for j in range(i + 1, len(string_list)):
            string2 = string_list[j]
            if sorted(string1.lower()) == sorted(string2.lower()) and len(string1) >= 3 and (len(string2) >= 3):
                anagram_pairs += 1
                if anagram_pairs > 9:
                    return False
    return anagram_pairs <= 9