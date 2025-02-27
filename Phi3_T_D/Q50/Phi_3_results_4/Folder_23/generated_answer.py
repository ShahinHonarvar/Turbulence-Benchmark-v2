from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def len_filter(string):
        return len(string) >= 3
    filtered = filter(len_filter, strings)
    sorted_filtered = [sorted(string.lower()) for string in filtered]
    anagram_groups = defaultdict(list)
    for index, value in enumerate(sorted_filtered):
        anagram_groups[value].append(index)
    count_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values() if len(group) >= 2))
    return count_pairs >= 67