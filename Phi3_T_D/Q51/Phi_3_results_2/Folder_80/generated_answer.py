from collections import defaultdict

def if_contains_anagrams(string_list):

    def get_sorted_key(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = defaultdict(int)
    for string in string_list:
        if len(string) >= 3:
            sorted_key = get_sorted_key(string)
            anagram_counts[sorted_key] += 1
    num_of_pairs = sum((v - 1 for v in anagram_counts.values())) // 2
    return num_of_pairs <= 255