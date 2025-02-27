from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_dict[''.join(sorted(word.lower()))].append(word)
    anagram_pairs = 0
    for words in anagram_dict.values():
        if len(words) > 1:
            anagram_pairs += len(words) * (len(words) - 1) // 2
    return anagram_pairs >= 42