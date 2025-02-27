def if_contains_anagrams(input_list):
    anagram_pairs = []
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if sorted(input_list[i].lower()) == sorted(input_list[j].lower()):
                anagram_pairs.append((input_list[i], input_list[j]))
    return len(anagram_pairs) <= 50