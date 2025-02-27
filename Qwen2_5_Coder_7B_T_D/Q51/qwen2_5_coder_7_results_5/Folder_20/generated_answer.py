def if_contains_anagrams(word_list):
    word_dict = {}
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in word_dict:
                word_dict[sorted_word] += 1
            else:
                word_dict[sorted_word] = 1
    pairs = sum([v * (v - 1) // 2 for v in word_dict.values()])
    return pairs <= 131