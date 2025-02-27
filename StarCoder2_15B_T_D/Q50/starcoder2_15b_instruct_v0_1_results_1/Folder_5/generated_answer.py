def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            string1 = string_list[i].lower()
            string2 = string_list[j].lower()
            if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1) == sorted(string2)):
                anagram_pairs += 1
                if anagram_pairs >= 21:
                    return True
    return False