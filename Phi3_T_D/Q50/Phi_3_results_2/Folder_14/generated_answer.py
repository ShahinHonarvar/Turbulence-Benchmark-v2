from collections import defaultdict

def if_contains_anagrams(strings):

    def clean_and_sort(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = clean_and_sort(string)
            anagram_dict[key].append(string)
    anagram_pairs = sum((len(v) >= 2 for v in anagram_dict.values()))
    return anagram_pairs >= 22