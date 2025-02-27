from collections import defaultdict

def if_contains_anagrams(strings):

    def count_sorted(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            anagram_dict[count_sorted(string)] += 1
    return sum((count > 1 for count in anagram_dict.values())) >= 209