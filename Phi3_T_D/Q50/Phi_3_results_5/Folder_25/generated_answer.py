from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower().replace(' ', '')) == sorted(s2.lower().replace(' ', ''))

    def sort_count(string):
        return ''.join(sorted(string.lower().replace(' ', '')))
    anagram_map = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            key = sort_count(string)
            anagram_map[key] += 1
    count_pairs = sum((v // 2 for v in anagram_map.values() if v >= 2))
    return count_pairs >= 14