from collections import defaultdict

def if_contains_anagrams(strings):

    def get_anagram_key(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            anagram_groups[get_anagram_key(string)].append(string)
    count_pairs = 0
    for group in anagram_groups.values():
        n = len(group)
        count_pairs += n * (n - 1) // 2
    return count_pairs >= 69