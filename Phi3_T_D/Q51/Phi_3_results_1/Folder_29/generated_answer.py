from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    sorted_strings = [sort_string(s) for s in strings if len(s) >= 3]
    anagram_counts = defaultdict(int)
    for s in sorted_strings:
        anagram_counts[s] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 318