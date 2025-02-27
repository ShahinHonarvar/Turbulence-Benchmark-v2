from collections import defaultdict

def if_contains_anagrams(strings):

    def count_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            anagram_counts[count_chars(string)] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) >= 64