from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_dict[sorted_chars(word)].append(word)
    pairs = 0
    for key, value in anagram_dict.items():
        if len(value) >= 2:
            pairs += len(value) * (len(value) - 1) // 2
    return pairs >= 19