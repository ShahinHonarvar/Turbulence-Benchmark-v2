from collections import defaultdict

def if_contains_anagrams(string_list):
    sorted_strings = [(''.join(sorted(s.lower())), s) for s in string_list if len(s) >= 3]
    counts = defaultdict(int)
    for key, value in sorted_strings:
        counts[key] += 1
    return sum((count > 1 for count in counts.values())) // 2 >= 66