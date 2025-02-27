from collections import defaultdict

def sort_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = sort_string(s)
            anagrams[key] += 1
    return sum((count - 1 for count in anagrams.values() if count >= 2)) >= 75