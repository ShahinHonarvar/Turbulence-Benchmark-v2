def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_dict.setdefault(normalized_word, []).append(word)
    anagram_pairs_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs_count <= 445