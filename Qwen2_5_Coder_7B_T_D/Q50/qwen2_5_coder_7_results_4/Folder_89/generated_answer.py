def if_contains_anagrams(lst):
    words = [word.lower() for word in lst if len(word) >= 3]
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs >= 36