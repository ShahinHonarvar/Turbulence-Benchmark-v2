from collections import defaultdict

def if_contains_anagrams(strings):

    def get_sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for string in strings:
        sorted_string = get_sorted_string(string)
        anagram_groups[sorted_string].append(string)
    anagram_count = sum([len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()])
    return anagram_count >= 178