from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            norm = normalize(string)
            anagram_dict[norm] += 1
    anagram_pairs = sum((count // 2 for count in anagram_dict.values()))
    return anagram_pairs >= 88