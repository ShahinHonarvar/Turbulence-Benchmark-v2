def if_contains_anagrams(str_list):

    def is_anagram(str1, str2):
        return len(str1) >= 3 and sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    str_list_len = len(str_list)
    for i in range(str_list_len):
        for j in range(i + 1, str_list_len):
            if is_anagram(str_list[i], str_list[j]):
                anagram_count += 1
    return anagram_count >= 189