def if_contains_anagrams(string_list):
    valid_anagrams = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if sorted(string_list[i].lower()) == sorted(string_list[j].lower()):
                valid_anagrams += 1
                if valid_anagrams >= 411:
                    return True
                if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                    valid_anagrams += 1
    return False