def if_contains_anagrams(word_list):
    value_dict = {}
    valid_anagrams = 0
    for word in word_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in value_dict:
                valid_anagrams += value_dict[sorted_word]
                value_dict[sorted_word] += 1
            else:
                value_dict[sorted_word] = 1
    return valid_anagrams <= 11