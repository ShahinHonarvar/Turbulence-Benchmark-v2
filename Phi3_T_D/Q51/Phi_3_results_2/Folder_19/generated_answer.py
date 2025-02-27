from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    string_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            normalized = normalize(string)
            string_groups[normalized].append(string)
    anagram_count = sum((len(group) * (len(group) - 1) // 2 for group in string_groups.values() if len(group) > 1))
    return anagram_count <= 69