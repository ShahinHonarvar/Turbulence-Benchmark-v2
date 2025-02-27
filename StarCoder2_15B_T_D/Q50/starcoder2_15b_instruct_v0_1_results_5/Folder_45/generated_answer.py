def if_contains_anagrams(string_list):
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            string1 = string_list[i].lower()
            string2 = string_list[j].lower()
            if len(string1) >= 3 and len(string2) >= 3:
                if sorted(string1) == sorted(string2):
                    return True
    return False