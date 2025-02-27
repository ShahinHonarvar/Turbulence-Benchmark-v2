from collections import defaultdict

def if_contains_anagrams(strings):

    def build_anagram_key(s):
        return ''.join(sorted(s.lower()))[::-1]

    def is_valid_length(s):
        return len(s) >= 3
    anagrams_count = defaultdict(int)
    for string in filter(is_valid_length, strings):
        key = build_anagram_key(string)
        anagrams_count[key] += 1
    return sum((count // 2 for count in anagrams_count.values())) >= 73