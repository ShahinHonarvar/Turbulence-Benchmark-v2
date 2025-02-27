def if_contains_anagrams(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and sorted_word in anagram_dict:
            anagram_dict[sorted_word] += 1
        elif len(word) >= 3:
            anagram_dict[sorted_word] = 1
    anagram_pairs = sum([v * (v - 1) // 2 for v in anagram_dict.values() if v > 1])
    return anagram_pairs <= 66