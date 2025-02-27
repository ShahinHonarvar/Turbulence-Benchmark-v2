from collections import defaultdict

def if_contains_anagrams(strings):

    def stringify(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    anagram_map = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            anagram_key = stringify(string)
            anagram_map[anagram_key] += 1
    num_pairs = sum((n * (n - 1) // 2 for n in anagram_map.values()))
    return num_pairs <= 17