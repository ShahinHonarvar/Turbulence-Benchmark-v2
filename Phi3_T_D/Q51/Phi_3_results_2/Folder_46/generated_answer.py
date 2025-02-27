def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = {}
    for word in words:
        if len(word) < 3:
            continue
        norm_word = normalize(word)
        if norm_word in anagram_dict:
            return True
        anagram_dict[norm_word] = [word]
    count_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values() if len(lst) > 1))
    return count_pairs <= 61