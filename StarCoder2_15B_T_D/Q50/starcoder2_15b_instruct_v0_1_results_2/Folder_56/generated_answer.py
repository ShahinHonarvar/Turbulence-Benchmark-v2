def if_contains_anagrams(input_list):
    pairs_of_anagrams = []
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if sorted(input_list[i].lower()) == sorted(input_list[j].lower()) and len(input_list[i]) >= 3:
                pairs_of_anagrams.append((input_list[i], input_list[j]))
    return len(pairs_of_anagrams) >= 77