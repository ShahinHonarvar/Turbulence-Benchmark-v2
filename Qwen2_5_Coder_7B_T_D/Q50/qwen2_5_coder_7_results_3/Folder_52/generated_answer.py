from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_dict[sorted_chars(word)].append(word)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values() if len(v) >= 2))
    return anagram_pairs >= 58