def if_contains_anagrams(input_list):
    anagram_pairs = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if sorted(input_list[i].lower()) == sorted(input_list[j].lower()) and len(input_list[i]) >= 3:
                anagram_pairs += 1
    return anagram_pairs >= 15