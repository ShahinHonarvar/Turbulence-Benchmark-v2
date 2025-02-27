def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            norm_word = normalize(word)
            anagram_dict[norm_word] = anagram_dict.get(norm_word, 0) + 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs <= 89