from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            anagram_dict[normalize(string)] += 1
    return sum((count // 2 for count in anagram_dict.values())) >= 30