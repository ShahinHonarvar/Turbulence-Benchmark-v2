from collections import defaultdict

def if_contains_anagrams(lst):

    def anagram_key(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_dict[anagram_key(word)].append(word)
    anagram_pairs_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs_count <= 407