from collections import defaultdict

def if_contains_anagrams(strings):

    def count_chars(s):
        count = defaultdict(int)
        for char in s.lower():
            count[char] += 1
        return frozenset(count.items())
    string_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            key = count_chars(string)
            string_counts[key] += 1
    return sum((v * (v - 1) // 2 for v in string_counts.values())) >= 188