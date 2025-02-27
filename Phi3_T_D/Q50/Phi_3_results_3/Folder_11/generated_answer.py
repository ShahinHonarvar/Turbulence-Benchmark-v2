from collections import defaultdict

def if_contains_anagrams(strings):

    def char_count(s):
        count = defaultdict(int)
        for char in s.lower():
            count[char] += 1
        return tuple(sorted(count.items()))
    anagram_dict = defaultdict(int)
    for string in strings:
        length = len(string)
        if length >= 3:
            anagram_dict[char_count(string)] += 1
    return sum((value > 1 for value in anagram_dict.values())) >= 28