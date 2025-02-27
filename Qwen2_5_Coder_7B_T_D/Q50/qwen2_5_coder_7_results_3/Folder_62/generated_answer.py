from collections import defaultdict

def if_contains_anagrams(lst):

    def sort_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = sort_chars(word)
            anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for key, value in anagram_dict.items():
        if len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs >= 43