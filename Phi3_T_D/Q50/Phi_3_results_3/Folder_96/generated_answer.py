from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def is_anagram_of_length(s, min_length):
        return len(s) >= min_length and normalize(s) in anagram_dict
    anagram_dict = defaultdict(list)
    for s in strings:
        if is_anagram_of_length(s, 3):
            anagram_dict[normalize(s)].append(s)
    found_anagrams = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            found_anagrams += len(anagrams) * (len(anagrams) - 1) // 2
    return found_anagrams >= 98