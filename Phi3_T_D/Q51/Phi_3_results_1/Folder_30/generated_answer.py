from collections import defaultdict

def sort_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_string = sort_string(string)
            anagram_counts[sorted_string] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 28