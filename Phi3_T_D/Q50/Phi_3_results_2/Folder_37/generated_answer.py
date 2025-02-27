from collections import defaultdict

def if_contains_anagrams(lst):

    def to_sorted_str(s):
        return ''.join(sorted(s.lower()))
    sorted_strings = [to_sorted_str(s) for s in lst if len(s) >= 3]
    frequencies = defaultdict(int)
    for string in sorted_strings:
        frequencies[string] += 1
    return sum((1 for count in frequencies.values() if count >= 2)) >= 29