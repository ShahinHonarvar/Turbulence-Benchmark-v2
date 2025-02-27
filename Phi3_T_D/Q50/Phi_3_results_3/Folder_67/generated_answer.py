from collections import defaultdict

def if_contains_anagrams(strings):
    string_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            string_counts[sorted_s] += 1
    return sum((count > 1 for count in string_counts.values())) >= 41