from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            sorted_anagrams[sorted_s].append(s)
    count = 0
    for key in sorted_anagrams:
        pairs = len(sorted_anagrams[key]) * (len(sorted_anagrams[key]) - 1) // 2
        count += pairs
    return count >= 188