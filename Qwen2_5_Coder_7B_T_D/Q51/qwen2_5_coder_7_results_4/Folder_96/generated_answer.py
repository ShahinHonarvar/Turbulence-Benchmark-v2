def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    word_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word] += 1
        else:
            word_dict[sorted_word] = 1
    anagram_pairs = [v for v in word_dict.values() if v > 1]
    return len(anagram_pairs) <= 2