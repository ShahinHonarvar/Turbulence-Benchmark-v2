from collections import defaultdict

def if_contains_anagrams(lst):

    def get_sorted_str(s):
        return ''.join(sorted(s.lower()))
    sorted_strings = [get_sorted_str(s) for s in lst if len(s) >= 3]
    counts = defaultdict(int)
    for sorted_str in sorted_strings:
        counts[sorted_str] += 1
    return sum((count // 2 for count in counts.values())) >= 94