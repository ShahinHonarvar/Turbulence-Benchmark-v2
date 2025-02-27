from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_dict[''.join(sorted(s.lower()))].append(s)
    anagram_pairs = 0
    for key, values in anagram_dict.items():
        if len(values) > 1:
            anagram_pairs += len(values) * (len(values) - 1) // 2
    return anagram_pairs >= 10