from collections import defaultdict

def if_contains_anagrams(lst):

    def count_anagrams(s):
        s = s.lower()
        sorted_str = ''.join(sorted(s))
        return sorted_str
    anagram_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagram_dict[count_anagrams(word)] += 1
    anagram_pairs = sum((1 for count in anagram_dict.values() if count > 1))
    return anagram_pairs >= 144