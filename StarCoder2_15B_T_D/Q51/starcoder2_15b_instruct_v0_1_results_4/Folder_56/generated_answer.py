def if_contains_anagrams(input_list):
    anagram_dict = {}
    for word in input_list:
        word_key = ''.join(sorted(word.lower()))
        if len(word_key) >= 3:
            if word_key in anagram_dict:
                anagram_dict[word_key] += 1
            else:
                anagram_dict[word_key] = 1
    return max(anagram_dict.values()) <= 11