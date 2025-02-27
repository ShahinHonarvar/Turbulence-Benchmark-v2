from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            normalized = normalize(string)
            anagram_dict[normalized] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs >= 24