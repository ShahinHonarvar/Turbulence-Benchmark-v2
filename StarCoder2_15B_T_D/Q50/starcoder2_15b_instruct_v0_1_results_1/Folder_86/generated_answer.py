def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if sorted(string_list[i].lower()) == sorted(string_list[j].lower()) and len(string_list[i]) >= 3 and (len(string_list[j]) >= 3):
                anagram_pairs += 1
    return anagram_pairs >= 115