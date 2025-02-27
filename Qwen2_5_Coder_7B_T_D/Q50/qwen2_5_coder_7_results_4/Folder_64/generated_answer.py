from collections import defaultdict

def if_contains_anagrams(strings):

    def get_sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = get_sorted_string(s)
            anagram_dict[sorted_str].append(s)
    anagram_pairs = 0
    for key, value in anagram_dict.items():
        if len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs >= 5