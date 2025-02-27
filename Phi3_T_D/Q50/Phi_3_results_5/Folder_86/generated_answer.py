from collections import defaultdict

def if_contains_anagrams(strings):

    def anagram_key(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            anagram_dict[anagram_key(string)].append(string)
    anagram_pairs = 0
    for _, items in anagram_dict.items():
        anagram_pairs += len(items) // 2
    return anagram_pairs >= 115