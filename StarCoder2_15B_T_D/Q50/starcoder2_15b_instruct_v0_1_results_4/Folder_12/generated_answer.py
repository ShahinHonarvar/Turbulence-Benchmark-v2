def if_contains_anagrams(input_list):
    anagram_pairs = []
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            str1 = input_list[i].lower()
            str2 = input_list[j].lower()
            if sorted(str1) == sorted(str2) and len(str1) >= 3:
                anagram_pairs.append((str1, str2))
    return len(anagram_pairs) >= 69