from collections import Counter

def if_contains_anagrams(lst):

    def count_anagrams(s):
        return Counter(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            signature = count_anagrams(word)
            if signature in anagram_dict:
                anagram_dict[signature].append(word)
            else:
                anagram_dict[signature] = [word]
    pairs = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            pairs += len(group) * (len(group) - 1) // 2
    return pairs >= 177