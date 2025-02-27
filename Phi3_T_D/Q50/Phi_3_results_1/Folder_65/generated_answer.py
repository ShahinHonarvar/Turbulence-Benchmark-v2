from collections import defaultdict

def if_contains_anagrams(string_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    is_anagram = defaultdict(int)
    for word in string_list:
        if len(word) >= 3:
            is_anagram[normalize(word)] += 1
    return sum((x * (x - 1) // 2 for x in is_anagram.values())) >= 94