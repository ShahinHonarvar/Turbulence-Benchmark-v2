def if_contains_anagrams(lst):

    def sort_word(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = {}
    for item in lst:
        if len(item) >= 3:
            sorted_item = sort_word(item)
            if sorted_item in anagram_dict:
                anagram_dict[sorted_item] += 1
            else:
                anagram_dict[sorted_item] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs <= 86