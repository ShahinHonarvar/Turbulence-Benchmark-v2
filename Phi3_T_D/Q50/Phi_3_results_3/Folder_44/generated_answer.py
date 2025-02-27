from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = defaultdict(int)
    count = 0
    for string in lst:
        sorted_str = ''.join(sorted(string.lower()))
        count += anagram_count[sorted_str]
        anagram_count[sorted_str] += 1
    return count >= 44