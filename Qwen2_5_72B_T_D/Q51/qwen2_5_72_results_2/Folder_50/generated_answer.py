def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized = normalize(word)
            anagram_dict.setdefault(normalized, []).append(word)
    anagram_pairs = sum((len(words) * (len(words) - 1) // 2 for words in anagram_dict.values()))
    return anagram_pairs <= 47