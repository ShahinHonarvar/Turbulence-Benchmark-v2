from collections import defaultdict

def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    length_filtered_strings = (s for s in strings if len(s) >= 3)
    groups_by_sorted_chars = defaultdict(list)
    for string in length_filtered_strings:
        sorted_chars = ''.join(sorted(string.lower()))
        groups_by_sorted_chars[sorted_chars].append(string)
    anagram_pairs = 0
    for group in groups_by_sorted_chars.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs >= 19