from collections import Counter

def if_contains_anagrams(strings_list):

    def sorted_tuple(s):
        return tuple(sorted(s.lower()))
    anagram_counts = Counter()
    for string in strings_list:
        if len(string) >= 3:
            sorted_str = sorted_tuple(string)
            anagram_counts[sorted_str] += 1
    num_at_least_two_pairs = sum((count // 2 for count in anagram_counts.values()))
    return num_at_least_two_pairs <= 94