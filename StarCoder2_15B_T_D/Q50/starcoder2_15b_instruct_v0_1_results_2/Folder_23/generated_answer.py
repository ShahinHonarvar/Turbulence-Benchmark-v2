def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            string_1 = string_list[i].lower()
            string_2 = string_list[j].lower()
            if len(string_1) >= 3 and len(string_2) >= 3:
                if sorted(string_1) == sorted(string_2):
                    anagram_pairs += 1
    return anagram_pairs >= 67