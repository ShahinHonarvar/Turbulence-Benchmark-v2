from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    string_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            for anagram in string_map[tuple(sorted(string.lower()))]:
                if is_anagram(string, anagram):
                    anagram_pairs += 1
            string_map[tuple(sorted(string.lower()))].append(string)
    return anagram_pairs <= 318