from collections import defaultdict

def if_contains_anagrams(strings):

    def count_sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_string = count_sorted_string(string)
            anagram_counts[sorted_string] += 1
    anagram_pairs = 0
    for count in anagram_counts.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 78