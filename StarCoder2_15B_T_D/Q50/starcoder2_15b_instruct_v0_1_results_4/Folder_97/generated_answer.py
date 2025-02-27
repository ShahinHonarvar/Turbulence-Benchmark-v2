def if_contains_anagrams(input_list):
    anagram_pairs = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            word1 = input_list[i].lower()
            word2 = input_list[j].lower()
            if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1) == sorted(word2)):
                anagram_pairs += 1
    return anagram_pairs >= 123