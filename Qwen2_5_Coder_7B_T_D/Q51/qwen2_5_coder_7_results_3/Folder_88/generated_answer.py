def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and sorted_word.isalpha():
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    anagram_pairs = sum([len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()])
    return anagram_pairs <= 407