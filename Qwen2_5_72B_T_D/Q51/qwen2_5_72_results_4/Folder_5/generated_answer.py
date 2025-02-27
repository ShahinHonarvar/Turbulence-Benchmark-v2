from collections import defaultdict

def if_contains_anagrams(strings):
    string_dict = defaultdict(int)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            string_dict[sorted_s] += 1
    anagram_pairs = sum((1 for count in string_dict.values() if count > 1))
    return anagram_pairs <= 4